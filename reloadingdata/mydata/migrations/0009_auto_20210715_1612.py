# Generated by Django 3.2.3 on 2021-07-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0008_auto_20210604_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='bullet',
            name='coal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bullet',
            name='landOffset',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bullet',
            name='landTotal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bullet',
            name='primer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]