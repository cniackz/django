from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from quickstart import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('quickstart/', include('quickstart.urls')),
]









    
    
