from django.urls import path
from .views import indexview, post_announcements, review_announcements,update_announcements, delete_announcements

urlpatterns = [
    path('',indexview, name='index'),
    path('announcements/',post_announcements, name='announcements'),
    path('review_announcements/',review_announcements, name='review_announcements'),
    path('update_announcements/<str:pk>/',update_announcements, name='update_announcements'),
    path('delete_announcements/<str:pk>/',delete_announcements, name='delete_announcements'),
    
]
