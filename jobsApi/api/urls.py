from django.urls import include, path

from jobsApi.api.views import *

urlpatterns = [
    path('jobs/', JobsListCreateAPIView.as_view(), name='jobs-list'),
    path('jobs/<int:pk>/', JobsDetailAPIView.as_view(), name='jobs-detail'),
]
