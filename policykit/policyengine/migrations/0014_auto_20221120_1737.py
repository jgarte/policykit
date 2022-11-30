# Generated by Django 3.2.2 on 2022-11-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policyengine', '0013_policyvariable_is_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyvariable',
            name='default_value',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='policyvariable',
            name='label',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='policyvariable',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='policyvariable',
            name='prompt',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='policyvariable',
            name='value',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
