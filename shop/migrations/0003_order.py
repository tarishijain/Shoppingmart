# Generated by Django 3.0.5 on 2020-05-11 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_category_cat_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=200)),
                ('products_id', models.CharField(max_length=200)),
                ('total', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('tax', models.IntegerField()),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('pincode', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
