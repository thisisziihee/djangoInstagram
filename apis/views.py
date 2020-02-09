from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@method_decorator(csrf_exempt, name = "dispatch")
class BaseView(View):
    @staticmethod
        # json 형식(key : value)의 response 만드는 것
        # 이제 이 BaseView를 상속받으면서 json 형식으로 만들면 됨
    def response(data = {}, message = '', status = 200):
        result = {
            'data' : data,
            'message' : message,
        }
        return JsonResponse(result, status = status)
