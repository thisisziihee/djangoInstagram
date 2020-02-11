from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Content, FollowRelation


@method_decorator(login_required, name = "dispatch")
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = self.request.user

        return context


@method_decorator(login_required, name = 'dispatch')
class RelationView(TemplateView):
    template_name = 'relation.html'
    def get_context_data(self, **kwargs):
        context = super(RelationView, self).get_context_data(**kwargs)
        user = self.request.user

        try:
            followers = FollowRelation.objects.get(follower = user).followee.all()
            context['followees'] = followers
            context['followees_id'] = list(followers.values_list('id', flat = True))

        except FollowRelation.DoesNotExist:
            pass 

        context['followers'] = FollowRelation.objects.select_related('folloewer').filter(followee__in = [user])
        return context

