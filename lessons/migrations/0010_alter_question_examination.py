# Generated by Django 5.0.7 on 2024-07-17 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_userquestion_answerforuq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='lessons.examination'),
        ),
    ]
