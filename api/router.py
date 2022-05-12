from rest_framework import routers
from .views import client_viewset

router=routers.DefaultRouter()
router.register('client',client_viewset)