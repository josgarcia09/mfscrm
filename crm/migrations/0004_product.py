# Generated by Django 4.1.2 on 2022-10-23 00:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_delete_product'),
    ]

    operations = [
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
