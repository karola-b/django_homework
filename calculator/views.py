from django.shortcuts import render, HttpResponse


def calculator(request):
    return HttpResponse("Welcome to my calculator")


def calculator_add(request, num1, num2):
    added_nums = num1 + num2
    return render(
        request,
        'add.html',
        context={
            "num1": num1,
            "num2": num2,
            "sum": added_nums
        }
    )