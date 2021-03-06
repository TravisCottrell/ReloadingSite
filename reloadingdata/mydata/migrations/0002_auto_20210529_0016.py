# Generated by Django 3.2.3 on 2021-05-29 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bullet',
            options={},
        ),
        migrations.AddField(
            model_name='testresults',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='testresults',
            name='gun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mydata.gun'),
        ),
        migrations.AlterField(
            model_name='bullet',
            name='gun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydata.gun'),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='bullet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mydata.bullet'),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='charge',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='moa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
