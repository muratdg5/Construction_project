# Generated by Django 4.1.7 on 2023-03-31 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_altservices_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AltServices',
        ),
    ]
