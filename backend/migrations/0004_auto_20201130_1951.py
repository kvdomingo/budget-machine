# Generated by Django 3.1.3 on 2020-11-30 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20201130_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incomeexpense',
            options={'ordering': ['-type', '-date'], 'verbose_name': 'income/expense', 'verbose_name_plural': 'incomes/expenses'},
        ),
    ]
