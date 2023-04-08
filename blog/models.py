from django.db import models
from django.utils.text import slugify

# Create your models here.
class Testimonials(models.Model):
    image=models.ImageField(upload_to='testimonials')
    name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    description=models.TextField()
    is_active=models.BooleanField(default=False)

class AboutSection(models.Model):
    title=models.CharField(max_length=200)
    date=models.CharField(max_length=100)
    title2=models.CharField(max_length=100)
    description=models.TextField()
    name1=models.CharField(max_length=100)
    name2=models.CharField(max_length=100)
    name3=models.CharField(max_length=100)
    description2=models.TextField()
    is_active=models.BooleanField(default=False)

class HeroSection(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='hero')
    image1=models.ImageField(upload_to='hero')
    image2=models.ImageField(upload_to='hero')
    image3=models.ImageField(upload_to='hero')
    image4=models.ImageField(upload_to='hero')
    image5=models.ImageField(upload_to='hero')
    is_active=models.BooleanField(default=False)


class Card(models.Model):
    image=models.ImageField(upload_to='card')
    title=models.CharField(max_length=200)
    description=models.TextField()
    is_active=models.BooleanField(default=False)

class Services(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    button=models.CharField(max_length=50)
    is_active=models.BooleanField(default=False)


class AltServices(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()


class OurProjectsCategory(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class OurProjects(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='ourprojects')
    description=models.TextField()
    is_active=models.BooleanField()
    is_home=models.BooleanField()
    category=models.ForeignKey(OurProjectsCategory, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.title}"





