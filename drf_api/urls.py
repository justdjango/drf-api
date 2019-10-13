from django.contrib import admin
from django.urls import path, include

from core.views import TestView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test')
]
