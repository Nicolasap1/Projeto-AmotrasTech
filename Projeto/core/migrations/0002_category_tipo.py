# Generated by Django 5.0.7 on 2024-08-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='tipo',
            field=models.CharField(db_column='tx_tipo', default=1, max_length=128, unique=True, verbose_name='tipo'),
            preserve_default=False,
        ),
    ]
