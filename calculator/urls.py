from django.urls import path

from . import views

urlpatterns = [
    path('add/<int:num1>/<int:num2>/', views.calculator_add),
    path('subtract/<int:num1>/<int:num2>/', views.subtract),
    path('divide/<int:num1>/<int:num2>/', views.divide),
    path('multiply/<int:num1>/<int:num2>/', views.multiply),
]
