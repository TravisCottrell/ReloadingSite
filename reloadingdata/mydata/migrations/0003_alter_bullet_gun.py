# Generated by Django 3.2.3 on 2021-05-29 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0002_auto_20210529_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bullet',
            name='gun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temp', to='mydata.gun'),
        ),
    ]
