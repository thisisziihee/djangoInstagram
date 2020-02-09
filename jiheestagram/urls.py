from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.shortcuts import redirect


class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return reidrect('home')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('apis.urls')),
    path('register/', NonUserTemplateView.as_view(template_name = 'register.html'), name = 'register'),
]
