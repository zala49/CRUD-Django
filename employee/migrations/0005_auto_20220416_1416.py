# Generated by Django 3.1.7 on 2022-04-16 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20220416_1349'),
        ('project', '0003_projectmodel_company'),
        ('department', '0002_auto_20220416_1349'),
        ('employee', '0004_auto_20220416_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.companymodel'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='department_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department.departmentmodel'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='project_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.projectmodel'),
        ),
    ]
