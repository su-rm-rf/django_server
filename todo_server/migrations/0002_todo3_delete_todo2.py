# Generated by Django 4.1 on 2023-04-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo2',
        ),
    ]
