# Generated by Django 4.0.3 on 2022-04-06 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daily_schedule', '0002_rename_autor_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyschedule',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]