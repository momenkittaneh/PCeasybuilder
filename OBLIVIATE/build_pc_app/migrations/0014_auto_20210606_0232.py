# Generated by Django 2.2.4 on 2021-06-05 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build_pc_app', '0013_merge_20210605_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orders',
            field=models.ManyToManyField(related_name='products', through='build_pc_app.cart', to='build_pc_app.order'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='order_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='build_pc_app.order'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='users_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycart', to='login_reg_app.users'),
        ),
        migrations.AlterField(
            model_name='product',
            name='build_pc',
            field=models.ManyToManyField(related_name='products', through='build_pc_app.cart', to='login_reg_app.users'),
        ),
    ]
