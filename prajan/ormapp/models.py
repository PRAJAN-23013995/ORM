from django.db import models
from django.contrib import admin
class bookdetails(models.Model):
       bookid=models.IntegerField()
       bookname=models.CharField(max_length=25)
       author=models.CharField(max_length=20)
       publishedyear=models.DateField()
       price=models.IntegerField()
       publishedcompany=models.CharField(max_length=20)
class bookdetailsAdmin(admin.ModelAdmin):
      list_display=("bookid","bookname","author","publishedyear","price","publishedcompany")
