# Generated by Django 2.1.2 on 2018-10-03 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_patch'),
    ]

    operations = [
        migrations.AddField(
            model_name='patch',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='patch_items', to='data.Item'),
        ),
    ]