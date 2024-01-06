from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.http.response import JsonResponse

# Create your views here.
@api_view(['GET'])
def index(request):
    articles_json = []

    articles_json = {'results': [
        {
            'id': '1',
            'title': 'TEST',
            'content': 'TEST CONTENT',
            'created_at': 0000,
            'updated_at': 1111,
        },
        {
            'id': '2',
            'title': 'TEST2',
            'content': 'TEST2 CONTENT',
            'created_at': 0000,
            'updated_at': 1111,
        },
    ]
    }
    return Response(articles_json, status=status.HTTP_200_OK)
    #return JsonResponse(articles_json, safe=False)


# decorators 관련해서도 잘 알아보고 다시 써야함
@api_view(['POST'])
@permission_classes([AllowAny])
def buy(request):
    lottoId = request.data.get('lottoId')
    lottoPw = request.data.get('lottoPw')
    lottoNum = request.data.get('lottoNum')
    print(lottoId, lottoPw, lottoNum)
    return Response(request.data, status=status.HTTP_200_OK)