from django.shortcuts import render, HttpResponse


def dashboard_index(request):
    return HttpResponse(f'سلام {request.user.get_full_name()}')
