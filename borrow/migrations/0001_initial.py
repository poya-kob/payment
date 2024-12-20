# Generated by Django 5.1.2 on 2024-11-09 11:23

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_code', models.UUIDField(auto_created=True, unique=True)),
                ('term', models.IntegerField(blank=True, null=True)),
                ('start_date', django_jalali.db.models.jDateField()),
                ('end_date', django_jalali.db.models.jDateField()),
                ('amount', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('status', models.CharField(choices=[('end', 'پایان یافته'), ('underwriting', 'درحال پذیره نویسی'), ('default', 'پیش فرض')], max_length=50)),
                ('number_of_loan_payable', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', django_jalali.db.models.jDateField()),
                ('refund_amount', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'در انتظار تایید'), ('approved', 'تایید شده'), ('rejected', 'رد شده'), ('paid', 'پرداخت شده'), ('default', 'پیش فرض')], max_length=50)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='borrow.loan')),
            ],
        ),
    ]
