from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.http.response import JsonResponse

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import system

# Create your views here.
@api_view(['GET'])
def index(request):
    weapon_info_list = list()
    weapon_info_list.append(system.test.api.get_weapon_info())
    print(weapon_info_list)
    return Response(weapon_info_list, status=status.HTTP_200_OK)
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