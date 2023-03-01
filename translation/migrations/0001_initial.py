# Generated by Django 3.2 on 2023-03-01 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languge', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TranslateDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/', verbose_name='file')),
                ('word_count', models.IntegerField(verbose_name='word_count')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('t_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trsn_from', to='translation.languges', verbose_name='Translation from')),
                ('t_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trsn_to', to='translation.languges', verbose_name='Translation to')),
            ],
        ),
    ]
