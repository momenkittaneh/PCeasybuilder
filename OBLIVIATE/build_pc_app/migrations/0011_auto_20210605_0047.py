# Generated by Django 2.2.4 on 2021-06-04 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_pc_app', '0010_auto_20210605_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='thumb',
            field=models.ImageField(upload_to='images/'),
        ),
    ]