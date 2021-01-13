from django.urls import include, path
from rest_framework import routers
from . import views
from .views import endpoint

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

	path('endpoint/', endpoint, name="countries"),
	
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]