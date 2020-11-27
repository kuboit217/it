# Generated by Django 3.1.2 on 2020-11-27 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0002_auto_20201127_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='requested',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='requested',
            name='time_rq',
            field=models.CharField(choices=[('1 ngày', '1 ngày'), ('2 ngày', '2 ngày'), ('3 ngày', '3 ngày'), ('Nhiều hơn 3 ngày', 'Nhiều hơn 3 ngày')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Nhanvien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
