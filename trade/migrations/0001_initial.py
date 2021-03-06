# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 12:26
from __future__ import unicode_literals

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
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Currency Name')),
            ],
        ),
        migrations.CreateModel(
            name='ExpireIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('hours', 'Hours'), ('minuts', 'minuts'), ('seconds', 'Seconds')], max_length=20, verbose_name='Expire Time Unit')),
                ('time', models.FloatField(default=0.0, verbose_name='Time')),
            ],
        ),
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('up', 'UP'), ('down', 'Down')], max_length=20, verbose_name='Direction')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[(0, 'Draft'), (1, 'Active'), (2, 'InActive'), (3, 'Win'), (4, 'Lose')], default=0, max_length=2)),
                ('currency', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='trade.Currency')),
                ('expire_in', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='trade.ExpireIN')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SignalBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[(0, 'Draft'), (1, 'Active'), (2, 'InActive'), (3, 'Win'), (4, 'Lose')], max_length=20, verbose_name='Status')),
                ('bid_amount', models.FloatField(default=0.0, verbose_name='Bid amount')),
                ('signal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='trade.Signal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('amount', models.FloatField(default=0.0, verbose_name='Bid amount')),
                ('type', models.CharField(choices=[('added', 'Added'), ('withdraw', 'Withdraw'), ('transfer', 'Transfer'), ('received', 'received')], max_length=50, verbose_name='Transaction Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
