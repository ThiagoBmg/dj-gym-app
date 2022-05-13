# Generated by Django 4.0.4 on 2022-05-13 03:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rep_qtd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('sets', models.ManyToManyField(blank=True, related_name='Set', to='app.set')),
            ],
        ),
    ]
