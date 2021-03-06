# Generated by Django 3.1.2 on 2020-11-28 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_nhanvien_part'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quanly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('part', models.CharField(choices=[('Nhân sự', 'Nhân sự'), ('Kế toán', 'Kế toán'), ('XNK', 'XNK'), ('Kho', 'Kho'), ('Thu mua', 'Thu mua')], max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Hoàn thành', 'Hoàn thành'), ('Chưa hoàn thành', 'Chưa hoàn thành'), ('Không chấp nhận', 'Không chấp nhận')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('nhanvien', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.nhanvien')),
                ('requested', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='request.requested')),
            ],
        ),
    ]
