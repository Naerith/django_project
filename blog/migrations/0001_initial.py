# Generated by Django 2.1.3 on 2018-12-01 08:00
# to make a migration: python manage.py makemigrations
# to run the migration that we have created: python manage.py migrate
# this will run a sqlcode on database, to see that code : python manage.py sqlmigrate blog 0001
# that will take class and write out the sql (object relational mapper)
# migration allow us to make changes on the database even there is data in it

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
