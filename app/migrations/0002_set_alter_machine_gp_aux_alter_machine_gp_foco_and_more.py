# Generated by Django 4.0.4 on 2022-05-13 02:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='machine',
            name='gp_aux',
            field=models.CharField(blank=True, choices=[('Peito', 'Peito'), ('Biceps', 'Biceps'), ('Triceps', 'Triceps'), ('Costas', 'Costas'), ('pos_perna', 'Posterior de Perna'), ('Perna', 'Perna')], default='Peito', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='gp_foco',
            field=models.CharField(choices=[('Peito', 'Peito'), ('Biceps', 'Biceps'), ('Triceps', 'Triceps'), ('Costas', 'Costas'), ('pos_perna', 'Posterior de Perna'), ('Perna', 'Perna')], default='Peito', max_length=500),
        ),
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
