# Generated by Django 4.2 on 2023-06-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userkey_user_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideamarks',
            name='score',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]