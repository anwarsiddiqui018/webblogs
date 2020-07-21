from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from MyApp.models import Post

from rest_framework.views import APIView
from rest_framework.response import Response


User = get_user_model()
post_list = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        qs_count_post = Post.objects.all().count()
        labels = ["Users","Post", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count,qs_count_post, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

