# Generated by Django 3.0.3 on 2020-03-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identite', '0008_auto_20200317_1313'),
        ('cahier_appel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appel',
            name='absent',
            field=models.ManyToManyField(blank=True, to='identite.Eleve'),
        ),
    ]