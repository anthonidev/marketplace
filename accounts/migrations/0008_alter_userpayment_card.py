# Generated by Django 3.2.6 on 2021-11-25 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211124_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpayment',
            name='card',
            field=models.CharField(max_length=19),
        ),
    ]