# Generated by Django 3.2.4 on 2021-06-23 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
