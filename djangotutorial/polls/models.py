from django.db import models
import uuid

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")


class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    models.IntegerField(default=0)


class Person(models.Model):
    person_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=20)
    
    def give_fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"
        
    
    def __str__(self) -> str:
        return self.give_fullname()

from django.core.exceptions import ValidationError

class Book(models.Model):
    book_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)

    def name_inappropriate(self):
        starts = ['sex', 'dead', 'fuck', 'down']
        return any(self.title.lower().startswith(word) for word in starts)

    def clean(self):
        if self.name_inappropriate():
            raise ValidationError("Inappropriate title detected. Please choose a different title.")

    def save(self, *args, **kwargs):
        self.clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

    
