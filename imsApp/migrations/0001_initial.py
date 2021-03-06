# Generated by Django 3.2.5 on 2021-07-23 12:29

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
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_model_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsApp.category')),
            ],
        ),
    ]
