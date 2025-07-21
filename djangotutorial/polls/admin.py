from django.contrib import admin

# Register your models here.
from .models import *


models = [
    Question, 
    Book, 
    Choise, 
    Person,
    Ram,
    Cpu,
    Gpu,
    Motherboard,
    Storage,
    PowerSupply,
    Case,
    Computer
]


for model in models:
    admin.site.register(model)
