from rest_framework import serializers
from .models import Quiz

 #Sirealize 시리얼라이즈는 장고의 모델 데이터를 json 타입으로 바꿔주는(직렬화) 코드입니다.

#QuizSerializer를 통해서 Quiz 모델의 데이터가 주어지면 밑의 요소들을 담고있는 json type data의 반환이 이루어집니다. 
class QuizSerializer(serializers.ModelSerializer):
     class Meta:
         model = Quiz
         fields = ('title', 'body', 'answer')

