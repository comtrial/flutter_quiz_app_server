from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response('HEllo world ')

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs =  Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)

    #위에서 받아온 randomQuizs의 직렬화 
    serializer = QuizSerializer(randomQuizs, many=True)

    return Response(serializer.data)