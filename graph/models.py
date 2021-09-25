from django.db import models


from initiatives.models import Initiative

import contractions
import nltk
import matplotlib.pyplot as plt                         # добавить в реквайрментс?
import re
import numpy as np
import pandas as pd
from datetime import datetime                           # для преобразования даты в строку, если надо?
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import TSNE


COMPARING_LIMIT = 0.05

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
                                                                    'pub_date', 'category_name')))

        ### Пункт 1: забьём на дату и адрес (и категорию?). Сконцентрируемся на имени и описании
        self.df = self.df[['id', 'name', 'description']]

        self.df['nlp_data'] = self.df['name'] + '. ' + self.df['description']
        self.df.drop('description', inplace=True, axis=1)


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

    def graph_dict(self):
        doc_sim_df = self.get_similarities_matrix()
        res = dict()
        for i in self.df['id'].values:
            res[i]=[]
            for j in self.df['id'].values[i:]:
                if doc_sim_df[i][j] > COMPARING_LIMIT:
                    if i in res.keys():
                        res[i].append(j)
                    else:
                        res[i] = [j]
                    if j in res.keys():
                        res[j].append(i)
                    else:
                        res[j] = [i]
        return res


if __name__ == '__main__':
    a = Graph()
    a.update()
