# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choose_date', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, null=True)),
                ('price', models.CharField(max_length=500, null=True)),
                ('long_duration', models.IntegerField(null=True)),
                ('date', models.CharField(max_length=500)),
                ('time', models.CharField(max_length=500, null=True)),
                ('url', models.URLField(null=True)),
                ('place', models.CharField(max_length=500, null=True)),
                ('event_type', models.CharField(max_length=500, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user_choices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=200, null=True)),
                ('user_title', models.CharField(max_length=200, null=True)),
                ('background', models.CharField(max_length=200, null=True)),
                ('font_colour', models.CharField(max_length=200, null=True)),
                ('font_size', models.CharField(max_length=200, null=True)),
                ('selected_event', models.ManyToManyField(to='webapp.event', through='webapp.choice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='conten',
            field=models.ForeignKey(to='webapp.event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='username',
            field=models.ForeignKey(to='webapp.user_choices'),
            preserve_default=True,
        ),
    ]
