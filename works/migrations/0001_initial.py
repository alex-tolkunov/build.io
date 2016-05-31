# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_amount', models.CharField(max_length=45, verbose_name='\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u043c\u043e\u0435 \u043a\u043e\u043b-\u0432\u043e \u0440\u0435\u0441\u0443\u0440\u0441\u0430 \u0434\u043b\u044f \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('real_amount', models.CharField(max_length=45, verbose_name='\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0435\u0441\u0443\u0440\u0441\u0430')),
            ],
            options={
                'db_table': 'resourses',
                'verbose_name': '\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0440\u0435\u0441\u0443\u0440\u0441\u044b',
                'verbose_name_plural': '\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0440\u0435\u0441\u0443\u0440\u0441\u044b',
            },
        ),
        migrations.CreateModel(
            name='ResoursesTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourse_name', models.CharField(max_length=45, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0441\u0443\u0440\u0441\u0430')),
            ],
            options={
                'db_table': 'resourses_types',
                'verbose_name': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0445 \u043d\u0430 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u0445',
                'verbose_name_plural': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0445 \u043d\u0430 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u0445',
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b')),
                ('plan_date', models.DateField(verbose_name='\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b')),
                ('end_date', models.DateField(verbose_name='\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0434\u0430\u0442\u0430 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b')),
                ('object_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Objects', verbose_name='\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043e\u0431\u044a\u0435\u043a\u0442')),
                ('teams_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Teams', verbose_name='\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u0431\u0440\u0438\u0433\u0430\u0434\u0430')),
                ('works_types_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.PropertiesTypes', verbose_name='\u0422\u0438\u043f \u0440\u0430\u0431\u043e\u0442\u044b, \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0439 \u0434\u043b\u044f \u043f\u043e\u0441\u0442\u0440\u043e\u0439\u043a\u0438')),
            ],
            options={
                'db_table': 'works',
                'verbose_name': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0444\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0440\u0430\u0431\u043e\u0442\u0430\u0445, \u043f\u0440\u043e\u0432\u043e\u0434\u0438\u043c\u044b\u0445 \u043f\u0440\u0438 \u0432\u043e\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432',
                'verbose_name_plural': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0444\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0440\u0430\u0431\u043e\u0442\u0430\u0445, \u043f\u0440\u043e\u0432\u043e\u0434\u0438\u043c\u044b\u0445 \u043f\u0440\u0438 \u0432\u043e\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='WorksTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type_name', models.CharField(max_length=45, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442\u044b')),
                ('object_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.ObjectTypes', verbose_name='\u0422\u0438\u043f \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043e\u0431\u044a\u0435\u043a\u0442\u0430')),
            ],
            options={
                'db_table': 'works_types',
                'verbose_name': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0445 \u043d\u0430 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u0445',
                'verbose_name_plural': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0445 \u043d\u0430 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u0445',
            },
        ),
        migrations.CreateModel(
            name='WorksTypesMachinesTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.MachinesTypes', verbose_name='\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0439 \u0442\u0438\u043f \u0442\u0435\u0445\u043d\u0438\u043a\u0438')),
                ('work_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.WorksTypes', verbose_name='\u0422\u0438\u043f \u0440\u0430\u0431\u043e\u0442\u044b')),
            ],
            options={
                'db_table': 'works_types_machines_types',
                'verbose_name': '\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0442\u0438\u043f\u044b \u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442',
                'verbose_name_plural': '\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0442\u0438\u043f\u044b \u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442',
            },
        ),
        migrations.AddField(
            model_name='resoursestypes',
            name='work_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.WorksTypes', verbose_name='\u0422\u0438\u043f \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AddField(
            model_name='resourses',
            name='resourse_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.ResoursesTypes', verbose_name='\u0420\u0435\u0441\u0443\u0440\u0441'),
        ),
        migrations.AddField(
            model_name='resourses',
            name='work_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.Works', verbose_name='\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u043c\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430'),
        ),
    ]
