from django.db import models
import uuid


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")


class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Person(models.Model):
    person_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)

    def give_fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.give_fullname()


from django.core.exceptions import ValidationError


class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)

    def name_inappropriate(self):
        starts = ["vv", "ccc", "qwe", "qws"]
        return any(self.title.lower().startswith(word) for word in starts)

    def clean(self):
        if self.name_inappropriate():
            raise ValidationError(
                "Inappropriate title detected. Please choose a different title."
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Ram(models.Model):
    ram_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    part_number = models.TextField(
        max_length=20,
    )
    brand_name = models.TextField(max_length=20)
    ram_name = models.TextField(max_length=10)
    capacity = models.IntegerField()
    ddr = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.brand_name},{self.ram_name}"


class Cpu(models.Model):
    cpu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.TextField(max_length=30)
    core_count = models.IntegerField()
    base_clock_speed = models.FloatField()
    socket_type = models.TextField(max_length=15)

    def __str__(self) -> str:
        return f"{self.model_name} ({self.core_count} cores)"


class Gpu(models.Model):
    gpu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.TextField(max_length=30)
    memory_size = models.IntegerField()
    chipset = models.TextField(max_length=20)

    def __str__(self):
        return f"{self.model_name} ({self.memory_size}GB)"


class Motherboard(models.Model):
    motherboard_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.TextField(max_length=30)
    socket_type = models.TextField(max_length=15)
    ram_slots = models.IntegerField()
    max_ram = models.IntegerField()

    def __str__(self):
        return self.model_name


class Storage(models.Model):
    storage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.TextField(max_length=30)
    capacity = models.IntegerField()
    storage_type = models.TextField(max_length=10)

    def __str__(self):
        return f"{self.model_name} ({self.capacity}GB {self.storage_type})"


class PowerSupply(models.Model):
    psu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.TextField(max_length=30)
    wattage = models.IntegerField()
    certification = models.TextField(max_length=10)

    def __str__(self):
        return f"{self.model_name} ({self.wattage}W)"


class Case(models.Model):
    case_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.TextField(max_length=30)
    form_factor = models.TextField(max_length=15)  # e.g. ATX, mATX
    color = models.TextField(max_length=15)

    def __str__(self):
        return f"{self.model_name} ({self.form_factor})"


class Computer(models.Model):
    computer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    computer_name = models.CharField(max_length=200, unique=True)
    computer_ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    computer_cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    computer_gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE)
    computer_psu = models.ForeignKey(PowerSupply, on_delete=models.CASCADE)
    computer_case = models.ForeignKey(Case, on_delete=models.CASCADE)
    computer_storage = models.ForeignKey(Storage, on_delete=models.CASCADE)

    def __str__(self):
        return self.computer_name


__all__ = [
    "Question",
    "Choise",
    "Person",
    "Book",
    "Ram",
    "Cpu",
    "Gpu",
    "Motherboard",
    "Storage",
    "PowerSupply",
    "Case",
    "Computer",
]
