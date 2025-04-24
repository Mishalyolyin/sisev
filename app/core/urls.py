from django.urls import path
from .views import stats_view, add_user, user_list, edit_user, delete_user


urlpatterns = [
    path('stats/', stats_view, name='stats'),
    path('add-user/', add_user, name='add_user'),
    path('users/', user_list, name='user_list'),  # ← new route
    path('users/<int:user_id>/edit/', edit_user, name='edit_user'),
    path('users/<int:user_id>/delete/', delete_user, name='delete_user'),

]