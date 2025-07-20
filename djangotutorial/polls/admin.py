from django.contrib import admin

# Register your models here.
from .models import Question,Book,Choise,Person


models=[Question,Book,Choise,Person]


for model in models:
    admin.site.register(model)

