from django.db import models

# Create your models here.

class Grades(models.Model):
    gname    = models.CharField(max_length=20) #CharField 字符串
    gdate    = models.DateTimeField()          #DateTimeField 日期类型
    ggirlnum = models.IntegerField()
    gboynum  = models.IntegerField           #整数型
    isDelete = models.BooleanField()        #布尔类型\


class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender  = models.BooleanField(default=True)
    sage     = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键  外键ForeingnKey
    sgrade   = models.ForeignKey("Grades",on_delete=models.CASCADE)



