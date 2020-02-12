from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Content, FollowRelation
from django.db.models import Prefetch


@method_decorator(login_required, name = "dispatch")
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = self.request.user

            # 내가 팔로우하는 사람들의 아이디를 리스트업한다.
        followees = FollowRelation.objects.filter(follower = user).values_list('followee__id', flat = True)

            # 내 아이디와 리스트업한 팔로우하는 사람들의 아이디를 합친다.
        lookup_user_ids = [user.id] + list(followees)

            # 내 아이디 + 팔로우들 아이디 로 필터를 걸고, 그에 해당하는 게시글을 저장한다.
            # select_related, prefetch_related 는 값을 가져오는 것..
        context['contents'] = Content.objects.select_related('user').prefetch_related('image_set').filter(
            user__id__in = lookup_user_ids
        )
        return context



    # 친구목록에 대한 로직
@method_decorator(login_required, name = 'dispatch')
class RelationView(TemplateView):
    template_name = 'relation.html'
    def get_context_data(self, **kwargs):
        context = super(RelationView, self).get_context_data(**kwargs)
        user = self.request.user
        print("RelationView user : ", user)

        try:
                #내가 팔로우하는(follower = user) 사람들 (followee) 불러오기
            followers = FollowRelation.objects.get(follower = user).followee.all()
            print("RelationView followees(내가 팔로우하는 사람들) : ", followers)
            context['followees'] = followers
            context['followees_ids'] = list(followers.values_list('id', flat = True))

        except FollowRelation.DoesNotExist:
            pass 

        context['followers'] = FollowRelation.objects.select_related('follower').filter(followee__in = [user])
            #나를 팔로우하는(followee__in = [user]) 사람들(followers)
        print("RelationView followers(나를 팔로우하는 사람들) : ",context['followers'])
        print("RelationView context :", context)
        return context

