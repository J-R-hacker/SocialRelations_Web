from django.db import models

'''
@Desc
    模型类
@Author monkey
@Date 2018-04-03
'''
# Create your models here.
# 存储
class Socialusers(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    chinesename = models.CharField(db_column='chineseName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(db_column='QQ', max_length=15, blank=True, null=True)  # Field name made lowercase.
    weibo = models.CharField(max_length=300, blank=True, null=True)
    identity_number = models.CharField(max_length=25, blank=True, null=True)
    cell_phone = models.CharField(max_length=20, blank=True, null=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    college = models.CharField(max_length=60, blank=True, null=True)
    living_place = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'SocialUsers'


# 用于表单查询的 model
CONDITION_CHOICES = (
    ('username', '用户名'),
    ('password', '密码'),
    ('chineseName', '姓名'),
    ('email', '邮箱'),
    ('QQ', 'QQ'),
    ('identity_number', '身份证'),
    ('cell_phone', '电话'),
    ('ip_address', 'IP 地址'),
    ('college', '大学'),
)

class QueryUser(models.Model):
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    queryContent = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return self.condition