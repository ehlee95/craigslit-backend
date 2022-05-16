from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from craigslitapp.views import PostViewSet


router = routers.DefaultRouter()
# registers a route that displays all posts
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
