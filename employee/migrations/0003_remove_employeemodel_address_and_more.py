# Generated by Django 4.0.4 on 2022-04-14 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('department', '0001_initial'),
        ('employee', '0002_alter_employeemodel_ph_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemodel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employeemodel',
            name='ph_number',
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='department_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='department.departmentmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='project_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.projectmodel'),
            preserve_default=False,
        ),
    ]