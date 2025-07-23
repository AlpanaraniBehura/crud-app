from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/employees', views.EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_create, name='employee_create'),
    path('edit/<int:pk>/', views.employee_update, name='employee_update'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('', include(router.urls)),
]
