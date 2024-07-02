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


def subtract(request, num1, num2):
    subtract_nums = num1 - num2
    return render(
        request,
        'subtract.html',
        context={
            "num1": num1,
            "num2": num2,
            "subtract": subtract_nums
        }
    )


def divide(request, num1, num2):
    divided_nums = num1 / num2
    return render(
        request,
        'divide.html',
        context={
            "num1": num1,
            "num2": num2,
            "division": divided_nums
        }
    )


def multiply(request, num1, num2):
    multiplied_nums = num1 * num2
    return render(
        request,
        'multiply.html',
        context={
            "num1": num1,
            "num2": num2,
            "multiply": multiplied_nums
        }
    )

