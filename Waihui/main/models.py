# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Language(models.Model):

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __unicode__(self):
        return self.english_name
    chinese_name = models.CharField( max_length=50)
    english_name = models.CharField( max_length=50)
    local_name = models.CharField( max_length=50)


class Provider(models.Model):

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __unicode__(self):
        return self.name
    user = models.OneToOneField(User)
    ROOKIE = 1
    APPLIED = 2
    INTERN = 3
    FORMAL = 4
    LEVELS_OF_TEACHER_CHOICES = (
        (ROOKIE,'非教师'),
        (APPLIED,'已申请'),
        (INTERN,'实习'),
        (FORMAL,'正式'),
    )
    status = models.IntegerField(max_length=2,
        choices=LEVELS_OF_TEACHER_CHOICES, 
        default=ROOKIE)
    name = models.CharField(max_length=50, )
    weekday_pattern = models.CommaSeparatedIntegerField(max_length=200)
    fee_rate = models.FloatField()
    hp = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def get_fee_rate(self):
        # "对该老师的fee_rate进行更新（在需要时）"
        return fee_rate


class Buyer(models.Model):

    class Meta:
        verbose_name = "Buyer"
        verbose_name_plural = "Buyers"

    def __unicode__(self):
        return self.nickname
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=50)
    brithday = models.DateField()
    mother_tongue = models.ForeignKey(Language)
    time_zone = models.CharField(max_length=50)
    hp = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def set_provider(self):
        new_provider = Provider;
        return 

class TopicCategory(models.Model):

    class Meta:
        verbose_name = "TopicCategory"
        verbose_name_plural = "TopicCategorys"

    def __unicode__(self):
        return self.name
    name = models.CharField( max_length=50)
    background_image = models.URLField()


class Topic(models.Model):

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        pass
    name = models.CharField(max_length=50)
    category = models.ForeignKey(TopicCategory)
    # default_plan = models.ForeignKey(Plan)
    status = models.IntegerField()
    creator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    


class Sku(models.Model):

    class Meta:
        verbose_name = "Sku"
        verbose_name_plural = "Skus"

    def __unicode__(self):
        return "("+u(self.start_time)+")"+self.topic
    provider = models.ForeignKey(Provider, )
    buyer = models.ForeignKey(Buyer)
    
    FORBOOK = 1
    PREBOOKED = 2
    REFUSED = 3
    LOSTED = 4
    BOOKED = 5
    PREPARED = 6
    FORVOTE = 7
    FINISHED = 8

    STATUS_OF_SKU_CHOICES = (
        (FORBOOK,'可预约'),
        (PREBOOKED,'已预约'),
        (REFUSED, '被拒绝扔池子的'),
        (LOSETD, '彻底没人教'),
        (BOOKED,'已定'),
        (PREPARED, '已备课'),
        (FORVOTE, '已结束代评价'),
        (FINISHED,'已彻底结束 '),
    )
    
    status = models.IntegerField(
        max_length=2,
        choices=STATUS_OF_SKU_CHOICES,
        default=FORBOOK,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    topic = models.ForeignKey(Topic)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Plan(models.Model):

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"

    def __unicode__(self):
        pass
    sku = models.OneToOneField(Sku ,blank=True, null=True)
    topic = models.ForeignKey(Topic, )
    status = models.IntegerField()
    content = models.TextField()
    assignment = models.TextField()
    slides = models.TextField()
    materiallinks = models.TextField()
    materialhtml = models.TextField()
    voc = models.TextField()
    copy_from = models.ForeignKey('self')
    # summary 写sum我怕出问题
    sumy = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Wallet(models.Model):

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"

    def __unicode__(self):
        return self.cny_balance
    user = models.ForeignKey(User)
    cny_balance = models.FloatField(default=0)
    display_currency = models.CharField( default= "CNY" , max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    

class ReviewTovProvider(models.Model):

    class Meta:
        verbose_name = "ReviewTovProvider"
        verbose_name_plural = "ReviewTovProviders"

    def __unicode__(self):
        return self.score
    provider = models.ForeignKey(Provider)
    buyer = models.ForeignKey(Buyer)
    sku = models.OneToOneField(Sku)
    questionnaire = models.CharField( max_length=50)
    comment = models.CharField(max_length=50)
    score = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def get_score(self):
        # questionnaire =
        pass 

class ReviewToBuyer(models.Model):

    class Meta:
        verbose_name = "ReviewToBuyer"
        verbose_name_plural = "ReviewToBuyers"

    def __unicode__(self):
        pass
    provider = models.ForeignKey(Provider)
    buyer = models.ForeignKey(Buyer)
    sku = models.OneToOneField(Sku)
    questionnaire = models.CharField( max_length=50)
    comment = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class ReplyToSku(models.Model):

    class Meta:
        verbose_name = "ReplyToSku"
        verbose_name_plural = "ReplyToSkus"

    def __unicode__(self):
        pass
    from_user = models.ForeignKey(User)
    from_type = models.IntegerField()
    content = models.TextField()
    to_reply = models.ForeignKey('self')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
# TODO 有空时咱们一起进行：
# 默认值、是否必填等有些还需要再调整
# max_length长度有些字段可能不够
# 添加日期、修改日期回头统一给每一个 model 加
# 最后再根据文档过一遍，看看还有哪里有遗漏

# TODO 添加方法（coolgene 将写出文档）
    
