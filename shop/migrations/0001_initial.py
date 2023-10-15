# Generated by Django 4.2.6 on 2023-10-15 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('slug', models.SlugField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('detail', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('categery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
