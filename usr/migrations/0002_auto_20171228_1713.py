# Generated by Django 2.0 on 2017-12-28 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CollageApp', '0001_initial'),
        ('usr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='password',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='students',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='userName',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='userName',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='students',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='userName',
        ),
        migrations.AddField(
            model_name='student',
            name='colleges',
            field=models.ManyToManyField(to='CollageApp.College'),
        ),
        migrations.AddField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usr.Parent'),
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usr.Teacher'),
        ),
    ]
