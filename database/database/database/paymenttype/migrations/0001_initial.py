# Generated by Django 4.0.3 on 2023-08-25 08:07

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('payment_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_type_display', models.CharField(max_length=100)),
                ('payment_type', multiselectfield.db.fields.MultiSelectField(choices=[('Registration', 'Registration'), ('Latefee', 'Latefee'), ('1st installment', '1st installment'), ('2nd installment', '2nd installment')], max_length=52)),
                ('payment_type_status', models.CharField(default='Active', max_length=10)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]