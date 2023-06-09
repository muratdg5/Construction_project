# Generated by Django 4.1.7 on 2023-03-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_aboutsection_is_active_card_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('button', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
