# Generated by Django 2.0.1 on 2018-01-28 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('employee_code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookProfile',
            fields=[
                ('serial_no', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('account_no', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('year_of_edition', models.PositiveIntegerField()),
                ('no_of_pages', models.PositiveIntegerField()),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BooksIssueReturnHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_code', models.CharField(max_length=50)),
                ('employee_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='booksissuereturnhistory',
            name='employee_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Employee'),
        ),
        migrations.AddField(
            model_name='booksissuereturnhistory',
            name='serial_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.BookProfile'),
        ),
    ]