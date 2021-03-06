# Generated by Django 3.1.7 on 2022-04-16 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20220416_1349'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentmodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.companymodel'),
        ),
        migrations.AlterField(
            model_name='departmentmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
