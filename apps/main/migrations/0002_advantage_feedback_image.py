# Generated by Django 5.1 on 2024-08-24 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='image',
            field=models.ImageField(default='1', upload_to='feedback'),
            preserve_default=False,
        ),
    ]
