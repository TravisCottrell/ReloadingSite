# Generated by Django 3.2.3 on 2021-05-30 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0006_rename_testresults_testresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='gun',
        ),
        migrations.AlterField(
            model_name='bullet',
            name='gun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bullets', to='mydata.gun'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='bullet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='results', to='mydata.bullet'),
        ),
    ]
