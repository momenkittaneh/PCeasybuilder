# Generated by Django 2.2.4 on 2021-06-06 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build_pc_app', '0014_auto_20210606_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='prodpic', to='build_pc_app.product'),
        ),
    ]
