# Generated by Django 4.1.2 on 2022-10-22 23:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('setup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('cleanup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('service_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('cust_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='crm.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('pickup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cust_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='crm.customer')),
            ],
        ),
    ]
