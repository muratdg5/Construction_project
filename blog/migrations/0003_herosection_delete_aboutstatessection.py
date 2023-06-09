# Generated by Django 4.1.7 on 2023-03-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_aboutsection_aboutstatessection'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='hero')),
                ('image1', models.ImageField(upload_to='hero')),
                ('image2', models.ImageField(upload_to='hero')),
                ('image3', models.ImageField(upload_to='hero')),
                ('image4', models.ImageField(upload_to='hero')),
                ('image5', models.ImageField(upload_to='hero')),
            ],
        ),
        migrations.DeleteModel(
            name='AboutStatesSection',
        ),
    ]
