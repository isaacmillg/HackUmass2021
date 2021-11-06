# Generated by Django 3.2.9 on 2021-11-06 21:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('info', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserGraphPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_id', models.CharField(default='', max_length=40, unique=True)),
                ('users', models.ManyToManyField(to='Users.User')),
            ],
        ),
    ]
