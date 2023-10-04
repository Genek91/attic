from django.urls import include, path
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
]
