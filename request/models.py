from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User
# Create your models here.

class Part(models.Model):
    PART =(
        ('Nhân sự', 'Nhân sự'),
        ('Kế toán', 'Kế toán'),
        ('XNK', 'XNK'),
        ('Kho', 'Kho'),
        ('Thu mua', 'Thu mua'),
    )     
    department = models.CharField(max_length=200, null=True,choices= PART)

    def __str__(self):
        return self.department

#tạo bảng nhân viên
class Nhanvien(models.Model):
    
    user = models.OneToOneField(User, blank=True, null=True, on_delete=SET_NULL)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    department = models.ForeignKey(Part, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



#tạo bảng requrest
class Requested(models.Model):
    TIME_RQ = (
        ('1 ngày', '1 ngày'),
        ('2 ngày', '2 ngày'),
        ('3 ngày', '3 ngày'),
        ('Nhiều hơn 3 ngày', 'Nhiều hơn 3 ngày'),
    )
    CATEGORY = (
        ('Có chi phí', 'Có chi phí'), 
        ('Bảo mật', 'Bảo mật'),
        ('Khác', 'Khác'),
    )
    STAR =(
        ('5 sao', '5 sao'),
        ('4 sao', '4 sao'),
        ('3 sao', '3 sao'),
        ('2 sao', '2 sao'),
        ('1 sao', '1 sao'),
    )
    nhanvien = models.ForeignKey(Nhanvien, null=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Part, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True,choices=CATEGORY)
    title = models.CharField(max_length=200, null=True)
    file = models.FileField(null=True)
    description = models.TextField(null=True)
    star = models.CharField(max_length=200, null=True, choices=STAR)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_accept = models.DateTimeField(null=True)
    date_closed = models.DateTimeField(null=True)
    time_rq = models.CharField(max_length=200, null=True, choices= TIME_RQ)

    def __str__(self):
        return self.name




class Status(models.Model):
    STATUS = (
        ('Hoàn thành', 'Hoàn thành'),
        ('Chưa hoàn thành', 'Chưa hoàn thành'),
        ('Không chấp nhận','Không chấp nhận')
    )
    nhanvien = models.ForeignKey(Nhanvien, null=True, on_delete=SET_NULL)
    requested = models.ForeignKey(Requested, null=True, on_delete=SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Quanly(models.Model):
  
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    department = models.ForeignKey(Part, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
