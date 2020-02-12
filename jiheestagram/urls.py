from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

from apis.views import UserLogoutView
from contents.views import HomeView, RelationView


class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('home')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('apis.urls')),
    path('', HomeView.as_view(), name = 'home'),
    path('register/', NonUserTemplateView.as_view(template_name = 'register.html'), name = 'register'),
    path('login/', NonUserTemplateView.as_view(template_name = 'login.html'), name = "login"),
    path('logout/', UserLogoutView.as_view(), name = "logout"),
    path('relation/', RelationView.as_view(), name = "relation" ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
