# Generated by Django 2.1.13 on 2021-03-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0003_auto_20210216_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=200)),
                ('desc', models.TextField()),
                ('image', models.ImageField(default='', upload_to='sunshine/images')),
            ],
        ),
    ]
