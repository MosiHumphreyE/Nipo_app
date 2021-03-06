# Generated by Django 2.0.5 on 2018-06-30 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('DateAdded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('reg_no', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('DateAdded', models.DateTimeField(auto_now_add=True)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nipo_student.School')),
            ],
        ),
    ]
