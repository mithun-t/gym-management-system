# Generated by Django 4.1.13 on 2024-06-09 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bicep', models.DecimalField(decimal_places=2, max_digits=5)),
                ('forearm', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shoulder', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chest', models.DecimalField(decimal_places=2, max_digits=5)),
                ('waist', models.DecimalField(decimal_places=2, max_digits=5)),
                ('thigh', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calf', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date_recorded', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'measurements',
            },
        ),
    ]