from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()

router.register('all', views.VaccineRecordViewSet) 
urlpatterns = [
    path('', include(router.urls)),
    path('order/<int:id>/', views.order_vaccine.as_view() ),
    
]

