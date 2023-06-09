# Generated by Django 4.1.2 on 2023-05-19 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='product')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
    ]
