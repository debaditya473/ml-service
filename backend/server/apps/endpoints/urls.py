# from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = router.urls

# urlpatterns = [
#     url(r"^api/v1/", include(router.urls)),
# ]

# from django.urls import path

# urlpatterns = [
#     path('endpoints', EndpointViewSet.as_view(), name = 'endpoints'),
#     path('mlalgorithms', MLAlgorithmViewSet.as_view(), name = 'mlalgorithms'),
#     path('mlalgorithmstatuses', MLAlgorithmStatusViewSet.as_view(), name = 'mlalgorithmstatuses'),
#     path('mlalgorithmstatuses', MLRequestViewSet.as_view(), name = 'mlalgorithmstatuses'),
# ]