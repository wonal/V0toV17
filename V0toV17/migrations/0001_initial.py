# Generated by Django 2.2.1 on 2019-06-01 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('notes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Techniques',
            fields=[
                ('technique_id', models.AutoField(primary_key=True, serialize=False)),
                ('technique', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dob', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Session_Techniques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='V0toV17.Session')),
                ('technique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='V0toV17.Techniques')),
            ],
        ),
        migrations.CreateModel(
            name='Climbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_success', models.IntegerField(default=0)),
                ('num_attempts', models.IntegerField(default=0)),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='V0toV17.Session')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='V0toV17.Users')),
            ],
        ),
    ]
