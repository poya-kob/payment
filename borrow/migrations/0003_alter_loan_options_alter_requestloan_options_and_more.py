# Generated by Django 5.1.2 on 2024-11-21 12:32

import django_jalali.db.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loan',
            options={'verbose_name': 'وام', 'verbose_name_plural': 'وام'},
        ),
        migrations.AlterModelOptions(
            name='requestloan',
            options={'verbose_name': 'درخواست ', 'verbose_name_plural': 'درخواست'},
        ),
        migrations.AddField(
            model_name='requestloan',
            name='pay_date',
            field=django_jalali.db.models.jDateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_code',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='requestloan',
            name='request_date',
            field=django_jalali.db.models.jDateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='requestloan',
            name='status',
            field=models.CharField(choices=[('warning', 'درحال بررسی'), ('dander', 'رد شده'), ('success', 'پرداخت شده'), ('default', 'پیش فرض')], max_length=50),
        ),
    ]