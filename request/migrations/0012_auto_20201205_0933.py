# Generated by Django 3.1.2 on 2020-12-05 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0011_auto_20201202_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='requested',
            name='it_member',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='request.part'),
        ),
        migrations.AlterField(
            model_name='quanly',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='request.part'),
        ),
        migrations.AlterField(
            model_name='requested',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='request.part'),
        ),
    ]
