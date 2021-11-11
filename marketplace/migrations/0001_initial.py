# Generated by Django 3.2.6 on 2021-11-10 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import marketplace.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=marketplace.models.marketplace_directory_path)),
                ('slug', models.SlugField(unique=True)),
                ('content_url', models.URLField(blank=True, null=True)),
                ('content_file', models.FileField(blank=True, null=True, upload_to='')),
                ('active', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField(default=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_purchased', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.product')),
            ],
        ),
    ]
