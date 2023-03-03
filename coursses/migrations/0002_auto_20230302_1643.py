# Generated by Django 3.2 on 2023-03-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursse',
            name='image',
            field=models.ImageField(default=' ', upload_to='coursses/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursse',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True),
        ),
    ]
