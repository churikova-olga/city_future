from django.contrib import admin

# Register your models here.
from .models import UserProfile, Answer, Question

admin.site.register(UserProfile)
admin.site.register(Question) #  вопросы
admin.site.register(Answer)