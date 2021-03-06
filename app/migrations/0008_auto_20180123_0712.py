# Generated by Django 2.0.1 on 2018-01-23 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20180123_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdate',
            name='event',
        ),
        migrations.AddField(
            model_name='bookdate',
            name='events',
            field=models.ManyToManyField(to='app.Event'),
        ),
        migrations.AddField(
            model_name='bookdate',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
