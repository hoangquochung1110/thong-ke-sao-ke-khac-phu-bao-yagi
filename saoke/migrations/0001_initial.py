# Generated by Django 5.1.1 on 2024-09-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('transaction_datetime', models.DateTimeField()),
                ('comment', models.TextField()),
                ('amount', models.DecimalField(decimal_places=15, max_digits=20)),
                ('offset_name', models.TextField(max_length=255)),
            ],
        ),
    ]
