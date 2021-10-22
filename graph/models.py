from django.db import models


from initiatives.models import Initiative

import contractions
import nltk                        # добавить в реквайрментс?
import re
import numpy as np
import pandas as pd
from datetime import datetime                           # для преобразования даты в строку, если надо?
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


COMPARING_LIMIT = 0.03


class Graph:

    def __init__(self):
        nltk.download('stopwords')
        self.stop_words = nltk.corpus.stopwords.words('russian')
        self.df = None
        self.update()

    """
    Обновить граф путём загрузки новых инициатив из базы данных.
    """
    def update(self):
        self.df = pd.DataFrame(list(Initiative.objects.all().values('id', 'name', 'description', 'address',
                                                                    'pub_date', 'category_name', 'rating')),
                               columns=['id', 'name', 'description', 'address', 'pub_date', 'category_name', 'rating'])

        ### Пункт 1: забьём на дату и адрес (и категорию?). Сконцентрируемся на имени и описании
        self.df = self.df[['id', 'name', 'description', 'category_name', 'rating']]

        self.df['nlp_data'] = self.df['name'] + '. ' + self.df['description'] + '. ' + self.df['category_name']

    """
        Функция, которая токенизирует текст
    """
    def _normalize_document(self, doc):
        # fix contractions
        doc = contractions.fix(doc)
        # remove special characters
        doc = re.sub(r'[^0-9а-яА-Я\s]', '', doc, flags=re.I | re.A)
        # lower case
        doc = doc.lower()
        # strip whitespaces
        doc = doc.strip()
        # tokenize document
        tokens = doc.split()
        # filter stopwords out of document
        # filtered_tokens = list(filter(None, [re.sub(r'[^A-Za-z]', '', token) for token in tokens]))
        filtered_tokens = list(token for token in tokens if token not in self.stop_words)
        # re-create document from filtered tokens
        doc = ' '.join(filtered_tokens)
        return doc

    def tfidf(self):
        normalize_corpus = np.vectorize(self._normalize_document)
        norm_corpus = normalize_corpus(list(self.df['nlp_data']))
        tv = TfidfVectorizer(min_df=0., max_df=1., norm='l2', use_idf=True)

        tfidf_matrix = tv.fit_transform(norm_corpus)
        tfidf_matrix = tfidf_matrix.toarray()

        return tfidf_matrix

    """
        Обновить граф путём загрузки новых инициатив из базы данных.
    """
    def get_similarities_matrix(self):
        self.update()
        tfidf_matrix = self.tfidf()
        doc_sim = cosine_similarity(tfidf_matrix)
        doc_sim_df = pd.DataFrame(doc_sim, columns=self.df['id'].values, index=self.df['id'].values)

        return doc_sim_df

    """
    Функция, создающая граф инициатив (ноды и соединения между ними).
    """
    def graph_dict(self, conditions=None):
        try:
            doc_sim_df = self.get_similarities_matrix()
        except ValueError:
            return {}, {}

        nodes, nodes_id = self.construct_nodes(doc_sim_df, conditions)
        edges = self.make_edges(doc_sim_df, nodes)

        return nodes, edges

    """
       Функция, создающая ноды.
       """
    def construct_nodes(self, table, conditions):
        nodes = []
        nodes_id = []
        # Добавляем сначала все элементы, удовлетворяющие условиям поиска
        for n in table.columns:
            if self.check_conditions(n, conditions):
                d = {
                    "font": {"color": "white"},
                    "id": n,
                    "label": self.df.loc[self.df['id'] == n].iat[0, 1].replace('\n', ''),
                    "shape": "dot",
                    "title": self.df.loc[self.df['id'] == n].iat[0, 2].replace('\r\n', '\u003cbr\u003e'),
                    "value": self.df.loc[self.df['id'] == n].iat[0, 4] * 10 + 100
                }
                nodes.append(d)
                nodes_id.append(n)

        # Далее добавляем все элементы из группы с уже сложенными:
        for node in nodes:
            for n in table.columns:
                if (table[node['id']][n] > COMPARING_LIMIT) and (n not in nodes_id):
                    d = {
                        "font": {"color": "white"},
                        "id": n,
                        "label": self.df.loc[self.df['id'] == n].iat[0, 1].replace('\n', ' '),
                        "shape": "dot",
                        "title": self.df.loc[self.df['id'] == n].iat[0, 2].replace('\r\n', '\u003cbr\u003e'),
                        "value": self.df.loc[self.df['id'] == n].iat[0, 4] * 10 + 100
                    }
                    nodes.append(d)
                    nodes_id.append(n)
        return nodes, nodes_id

    """
    Функция, соединяющая ноды.
    """
    @staticmethod
    def make_edges(table, nodes):
        edges = []
        for node1 in nodes:
            for node2 in nodes:
                if (table[node1['id']][node2['id']] > COMPARING_LIMIT) and (node1['id'] != node2['id']):
                    e = {
                        "from": node1['id'],
                        "to": node2['id'],
                        "value": int(table[node1['id']][node2['id']]*100)
                    }
                    edges.append(e)
        return edges

    """
    Функция проверки условий.
    """
    def check_conditions(self, n, conditions: dict):   # TODO: Сделать фильтры для сравнения ">" или "<", но стоит ли?
        res = True
        if conditions:
            for field, val in conditions.items():
                if field != 'name':
                    if self.df.loc[self.df['id'] == n].iloc[0][field] != val:
                        res = False
                        break
                else:
                    if val not in self.df.loc[self.df['id'] == n].iloc[0][field]:
                        res = False
                        break
        return res





