  
# Generated by Django 3.2.1 on 2021-05-08 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beds', '0002_auto_20210506_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]