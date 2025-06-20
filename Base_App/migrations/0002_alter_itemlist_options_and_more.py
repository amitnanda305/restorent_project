# Generated by Django 5.2 on 2025-06-18 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemlist',
            options={'verbose_name': 'Item Category', 'verbose_name_plural': 'Item Categories'},
        ),
        migrations.RenameField(
            model_name='items',
            old_name='Item_name',
            new_name='item_name',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='Price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='items',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='items',
            name='Image',
        ),
        migrations.AddField(
            model_name='feedback',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='feedback/'),
        ),
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Base_App.itemlist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='image',
            field=models.ImageField(default=1, upload_to='items/'),
            preserve_default=False,
        ),
    ]
