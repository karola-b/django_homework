from django.shortcuts import render


def business_card(request):
    return render(
        request,
        'business_card.html'
    )
