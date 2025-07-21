from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse, Http404
from .models import *
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, filters
from rest_framework.response import Response
from .serializers import *


def nikosTes(request):
    html_content = """
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f9;
                }
                .container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .my-div {
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    text-align: center;
                    font-size: 24px;
                }
                .my-div:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="my-div">
                    Welcome to Nikos' Test Page!
                </div>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html_content)


def biography(request):
    return render(request, "polls/biography.html")


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


class UserViewSet(viewsets.ModelViewSet):
    """endpoint tha allows users to be viewed or edited"""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """API endpoint that allows books to be viewed, edited, deleted, or updated"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []

    def destroy(self, request, *args, **kwargs):
        """Custom behavior for DELETE"""
        instance = self.get_object()

        instance.delete()
        return Response({"message": "Book deleted successfully"}, status=204)

    def update(self, request, *args, **kwargs):
        """Custom behavior for PUT (update)"""
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.order_by("computer_name")
    serializer_class = ComputerSerializer
    permission_classes = []


class RamViewSet(viewsets.ModelViewSet):
    queryset = Ram.objects.order_by("part_number")
    serializer_class = RamSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ["part_number", "brand_name", "ram_name"]

    def destroy(self, request, *args, **kwargs):
        """Custom behavior for DELETE"""
        instance = self.get_object()
        instance.delete()
        return Response({"message": "RAM deleted successfully"}, status=204)


class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer
    permission_classes = []


class GpuViewSet(viewsets.ModelViewSet):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer
    permission_classes = []


class MotherBoardViewSet(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherBoardSerializer
    permission_classes = []


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = []


class PowerSupplyViewSet(viewsets.ModelViewSet):
    queryset = PowerSupply.objects.all()
    serializer_class = PowerSupplySerializer
    permission_classes = []


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = []
