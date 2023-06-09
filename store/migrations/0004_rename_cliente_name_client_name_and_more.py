# Generated by Django 4.1.7 on 2023-03-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_name_client_cliente_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='cliente_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='total_to_pay',
        ),
        migrations.AlterField(
            model_name='buy',
            name='card_holder_name',
            field=models.CharField(help_text='Buy card_holder_name', max_length=256, verbose_name='Card_holder_name'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='card_number',
            field=models.CharField(help_text='Buy card_number', max_length=256, verbose_name='Card_number'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='cvv',
            field=models.CharField(help_text='Buy cvv', max_length=3, verbose_name='Cvv'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='exp_date',
            field=models.CharField(help_text='Buy exp_date', max_length=4, verbose_name='Exp_date'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='value',
            field=models.DecimalField(decimal_places=2, help_text='Buy value', max_digits=10000, verbose_name='Value'),
        ),
    ]
