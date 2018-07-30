from django.db import models

# Create your models here.

class ZhaoPin(models.Model):

    url = models.CharField(max_length=1000,null=True)
    url_id = models.CharField(max_length=255,null=True,unique=True)
    pname = models.CharField(max_length=255,null=True)
    smoney = models.IntegerField(null=True)
    emoney = models.IntegerField(null=True)
    location = models.CharField(max_length=255,null=True)
    syear = models.IntegerField(null=True)
    eyear = models.IntegerField(null=True)
    degree = models.CharField(max_length=255,null=True)
    ptype = models.CharField(max_length=255,null=True)
    tags = models.CharField(max_length=255,null=True)
    date_pub = models.DateField(null=True)
    advantage = models.CharField(max_length=1000,null=True)
    jobdesc = models.TextField(null=True)
    jobaddr = models.CharField(max_length=255,null=True)
    company = models.CharField(max_length=255,null=True)
    spider_name = models.CharField(max_length=255,null=True)
    crawl_time = models.DateField(null=True)
    ages = models.CharField(max_length=255,null=True)
    planguage = models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'lagou_job'
