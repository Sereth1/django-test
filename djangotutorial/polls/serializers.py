from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import (
    Book,
    Ram,
    Cpu,
    Gpu,
    Motherboard,
    Storage,
    PowerSupply,
    Case,
    Computer,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["book_id", "title"]


class ComputerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Computer
        fields = [
            "computer_id",
            "computer_name",
            "computer_ram",
            "computer_cpu",
            "computer_gpu",
            "computer_psu",
            "computer_case",
            "computer_storage",
        ]


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = ["ram_id", "part_number", "brand_name", "ram_name", "ddr", "capacity"]


class CpuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cpu
        fields = ["cpu_id", "model_name", "core_count", "base_clock_speed", "socket_type"]


class GpuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gpu
        fields = ["gpu_id", "model_name", "memory_size", "chipset"]


class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = [
            "motherboard_id",
            "model_name",
            "socket_type",
            "ram_slots",
            "max_ram",
        ]


class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = [
            "storage_id",
            "model_name",
            "capacity",
            "storage_type",
        ]


class PowerSupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = PowerSupply
        fields = [
            "psu_id",
            "model_name",
            "wattage",
            "certification",
        ]


class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = [
            "case_id",
            "model_name",
            "form_factor",
            "color",
        ]


__all__ = [
    "RamSerializer",
    "BookSerializer",
    "GroupSerializer",
    "UserSerializer",
    "UserSerializer",
    "GroupSerializer",
    "BookSerializer",
    "CpuSerializer",
    "ComputerSerializer",
    "CaseSerializer",
    "GpuSerializer",
    "MotherBoardSerializer",
    "PowerSupplySerializer",
    "StorageSerializer",
]
