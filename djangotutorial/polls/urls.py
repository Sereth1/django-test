from django.urls import path, include
from rest_framework import routers

from . import views
from . import test

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'books',views.BookViewSet)
urlpatterns = [
    path("lol/", views.nikosTes, name="nikosTes"),
    path("test/", test.testing, name="testing"),
    path("bio/", views.biography, name="biography"),
    path("", views.index, name="index"),
    path('api/', include(router.urls)),  # Add this line
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]