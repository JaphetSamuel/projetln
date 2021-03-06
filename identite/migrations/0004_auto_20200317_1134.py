# Generated by Django 3.0.3 on 2020-03-17 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('identite', '0003_auto_20200317_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='etablissement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='identite.Etablissement'),
        ),
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identite.Etablissement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
