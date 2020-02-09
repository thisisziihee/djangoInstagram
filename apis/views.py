from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from django.core.validators import validate_email, ValidationError
from django.db import IntegrityError
from django.contrib.auth.models import User



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


class UserCreateView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        username = request.POST.gt('username', '')
        if not username:
            return self.response(message = '아이디를 입력하세요.', status = 400)
        
        password = request.POST.get('password', '')
        if not password:
            return self.response(message = '비밀번호를 입력하세요.', status = 400)

        email = request.POST.get('email', '')
        try :
            validate_email(email)
        except ValidationError:
            return self.response(message = "올바른 이메일을 입력하세요.", status = 400)

        try :
            user = User.objects.create_user(username = username, email = email, password = password)
        except IntegrityError:
            return self.response(message = "이미 존재하는 아이디입니다.", status = 400)

        return self.response({'user.id' : user.id})