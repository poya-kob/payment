# Generated by Django 5.1.2 on 2024-11-09 11:23

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('borrow', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InstallmentRePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('payment', models.DecimalField(decimal_places=3, max_digits=10)),
                ('pay_date', django_jalali.db.models.jDateField()),
                ('upload_date', django_jalali.db.models.jDateField()),
                ('is_verified', models.BooleanField(default=False)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='borrow.loan')),
            ],
        ),
    ]