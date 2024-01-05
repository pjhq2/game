from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', obtain_auth_token, name='login') # 나중에 Custom Auth Token으로 변경하기
]
