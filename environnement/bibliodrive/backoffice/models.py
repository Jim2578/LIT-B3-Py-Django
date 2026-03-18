from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    year_born = models.SmallIntegerField()

class Title(models.Model):
    title = models.CharField(max_length=255)
    year_published = models.SmallIntegerField()
    isbn = models.CharField(primary_key=True, max_length=20)
    pubid = models.IntegerField()
    description = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    comments = models.TextField()
    pubid = models.ForeignKey("Publishers", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author", related_name="title_authors", blank=True, default=None)
    reserved = models.BooleanField(default=False)


class Publishers(models.Model):
    pubid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    compagny_name = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    zip = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    comments = models.TextField()
