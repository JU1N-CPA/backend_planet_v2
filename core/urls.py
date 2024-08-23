from django.urls import re_path

from core.views import user_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # re_path(r'^api/members', User.get_all_members),
    # url(r'^api/members/(?P<pk>[0-9]+)$', members_view.get_all_members),
    re_path('logout/', user_view.logout, name='logout'),
    re_path('login/', user_view.login, name='login'),
    re_path('signup/', user_view.signup, name='create_user'),
    re_path('user/', user_view.profile, name='user'),

]
