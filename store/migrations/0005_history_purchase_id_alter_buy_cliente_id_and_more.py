# Generated by Django 4.1.7 on 2023-03-20 14:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_cliente_name_client_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='purchase_id',
            field=models.ForeignKey(help_text='Purchase_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='store.buy', verbose_name='Purchase_id'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='cliente_id',
            field=models.ForeignKey(help_text='Cliente', on_delete=django.db.models.deletion.CASCADE, to='store.client', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
