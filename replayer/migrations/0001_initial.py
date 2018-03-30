# Generated by Django 2.0.3 on 2018-03-29 09:21

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.CharField(default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.CharField(default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.CharField(default='', max_length=500, null=True)),
                ('results', jsonfield.fields.JSONField(default={})),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trace_log', to='replayer.Log')),
            ],
        ),
    ]