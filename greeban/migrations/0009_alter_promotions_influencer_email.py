# Generated by Django 3.2.8 on 2021-10-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greeban', '0008_promotions_influencer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotions',
            name='influencer_email',
            field=models.CharField(default='', max_length=50),
        ),
    ]