from django.urls import include, path
from . import views

app_name = 'api'

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    
    path('', views.index, name='index'),
    path('buy/', views.buy, name='buy'),
]
