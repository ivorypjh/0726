from django.db import models

# Create your models here.

# 클래스를 생성할 때는 models.Model 을 상속해야 함
class Item(models.Model):
    # 이름은 테이블 이름이고 필드는 자료형
    # Char 는 max_length를 반드시 설정해줘야 함
    # primary_key 는 기본키 설정
    itemid = models.CharField(max_length=50, primary_key=True)
    itemname = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    pricureUrl = models.CharField(max_length=50)