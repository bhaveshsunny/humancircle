# Generated by Django 2.0.1 on 2018-01-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180123_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdate',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookdate',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
