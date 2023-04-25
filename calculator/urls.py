from django.urls import path

from . import views

urlpatterns = [
    path('add/<int:num1>/<int:num2>/', views.calculator_add),
    path('subtract/<int:num1>/<int:num2>', views.subtract)
]
