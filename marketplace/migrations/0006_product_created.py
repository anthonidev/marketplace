# Generated by Django 3.2.6 on 2021-11-14 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_alter_reviews_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
