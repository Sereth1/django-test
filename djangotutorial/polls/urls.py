from django.urls import path, include
from rest_framework import routers

from . import views
from . import test

router = routers.DefaultRouter()


routes = [
    ("users", views.UserViewSet),
    ("groups", views.GroupViewSet),
    ("books", views.BookViewSet),
    ("Computer", views.ComputerViewSet),
    ("Ram", views.RamViewSet),
    ("Cpu", views.CpuViewSet),
    ("Gpu", views.GpuViewSet),
    ("MotherBoard", views.MotherBoardViewSet),
    ("Storage", views.StorageViewSet),
    ("PowerSupply", views.PowerSupplyViewSet),
    ("Case", views.CaseViewSet),
]


for route, viewset in routes:
    router.register(route, viewset)

basic_routes = [
    ("lol/", views.nikosTes, "nikosTes"),
    ("test/", test.testing, "testing"),
    ("bio/", views.biography, "biography"),
    ("", views.index, "index"),
    ("<int:question_id>/", views.detail, "detail"),
    ("<int:question_id>/results/", views.results, "results"),
    ("<int:question_id>/vote/", views.vote, "vote"),
]

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

for route, view_func, name in basic_routes:
    urlpatterns.append(path(route, view_func, name=name))
