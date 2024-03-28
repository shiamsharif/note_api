from rest_framework import routers
from Note import views

router = routers.DefaultRouter()
router.register(r'', views.NoteViewSet, basename='note')

urlpatterns = router.urls