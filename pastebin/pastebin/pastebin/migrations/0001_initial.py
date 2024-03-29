# Generated by Django 3.0.1 on 2019-12-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('title', models.CharField(blank=True, max_length=30)),
                ('syntax', models.IntegerField(choices=[(0, 'Plain'), (1, 'Python'), (2, 'HTML'), (3, 'SQL'), (4, 'Javascript'), (4, 'Plain')], default=0)),
                ('poster', models.CharField(blank=True, max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
