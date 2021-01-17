from django.db import models

#순서의 진행
#1. model의 구체화
#2. views의 형성
#3. url의 설정

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    

    #Sirealize 시리얼라이즈는 장고의 모델 데이터를 json 타입으로 바꿔주는(직렬화) 코드입니다.