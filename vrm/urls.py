from django.urls import path, include
from .views import home_views
from .viewsets import UserViewSet, CourseViewSet


urlpatterns = [
    
    path('profile/', UserViewSet.as_view({'get':'get'})),
    path('course/', CourseViewSet.as_view({'get':'get'}))   
]