from django.contrib import admin
from django.urls import path
from app.views import sample_data, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sample-data/', sample_data, name='sample_data'),
    path('', index, name='index'),
]
