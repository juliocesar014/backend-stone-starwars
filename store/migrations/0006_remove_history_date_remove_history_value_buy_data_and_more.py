# Generated by Django 4.1.7 on 2023-03-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_history_purchase_id_alter_buy_cliente_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='date',
        ),
        migrations.RemoveField(
            model_name='history',
            name='value',
        ),
        migrations.AddField(
            model_name='buy',
            name='data',
            field=models.DateField(help_text='History data', null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='value',
            field=models.DecimalField(decimal_places=2, help_text='History value', max_digits=10000, verbose_name='Value'),
        ),
    ]
