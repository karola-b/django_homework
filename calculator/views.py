from django.shortcuts import render, HttpResponse


def calculator(request):
    return HttpResponse("Welcome to my calculator")
