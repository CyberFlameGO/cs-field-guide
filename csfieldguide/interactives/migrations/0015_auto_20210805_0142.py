# Generated by Django 2.2.22 on 2021-08-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactives', '0014_auto_20191008_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactive',
            name='name_xx_lr',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='interactive',
            name='name_yy_rl',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='interactive',
            name='template_xx_lr',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='interactive',
            name='template_yy_rl',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
