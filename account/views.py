from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from django.core import serializers
import json
User = get_user_model()
# Create your views here.


def users(request):
    user = {
        "name": "John Doe",
        "age": 30,
        "profession": "Software Engineer",
        "location": "New York",
        "hobbies": ["Reading", "Traveling", "Gaming"],
    }
    users = User.objects.all()
    user_list = serializers.serialize('json', users)
    user_json = json.loads(user_list)
    print(user_json)
    return JsonResponse(user_json)
