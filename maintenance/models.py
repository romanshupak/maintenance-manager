from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("maintenance:department-detail", kwargs={"pk": self.pk})


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)
    duties = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("maintenance:position-detail", kwargs={"pk": self.pk})


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
        blank=False,
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name} {self.position.name})"

    def get_absolute_url(self):
        return reverse("maintenance:worker-detail", kwargs={"pk": self.pk})


class Maintenance(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="maintenances"
    )
    person_in_charge = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="maintenances"
    )

    class Meta: 
        ordering = ("name", )

    def get_absolute_url(self):
        return reverse("maintenance:maintenance-detail", kwargs={"pk": self.pk})
