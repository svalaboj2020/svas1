# Generated by Django 3.0.7 on 2020-07-05 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mother_name', models.CharField(max_length=20)),
                ('m_email', models.EmailField(max_length=30)),
                ('m_phone', models.CharField(max_length=14)),
                ('father_name', models.CharField(max_length=20)),
                ('f_email', models.EmailField(max_length=30)),
                ('f_phone', models.CharField(max_length=14)),
                ('guardian_name', models.CharField(max_length=20)),
                ('g_email', models.EmailField(max_length=30)),
                ('g_phone', models.CharField(max_length=14)),
            ],
        ),
    ]
