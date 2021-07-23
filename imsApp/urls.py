from django.urls import path
from imsApp.views import CategoryAPI,ProductAPI

urlpatterns = [
    path('category/', CategoryAPI.as_view() ),
    path('product/', ProductAPI.as_view() ),
]