# Generated by Django 3.2 on 2023-03-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0003_auto_20230301_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translatedb',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]