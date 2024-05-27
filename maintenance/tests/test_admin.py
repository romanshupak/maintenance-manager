from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from maintenance.models import Department, Position, Worker, Maintenance


class AdminTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin"
        )
        self.client.force_login(self.admin_user)

        self.department = Department.objects.create(name="Test Department")
        self.position = Position.objects.create(name="Test Position")

        # Створюємо робітника з екземпляром позиції
        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="testworker",
            first_name="Test",
            last_name="Worker",
            position=self.position
        )

        self.maintenance = Maintenance.objects.create(
            name="Test Maintenance",
            description="Test description",
            deadline=date.today(),
            is_completed=False,
            department=self.department,
        )

    def test_department_admin(self):
        url = reverse("admin:maintenance_department_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.department.name)

    def test_position_admin(self):
        url = reverse("admin:maintenance_position_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.position.name)

    def test_worker_admin(self):
        url = reverse("admin:maintenance_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.username)
        self.assertContains(res, self.worker.position.name)

    def test_worker_admin_additional_info(self):
        url = reverse("admin:maintenance_worker_change", args=[self.worker.id])
        res = self.client.get(url)
        self.assertContains(res, "Additional info")
        self.assertContains(res, self.worker.position.name)

    def test_maintenance_admin(self):
        url = reverse("admin:maintenance_maintenance_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.maintenance.name)
        self.assertContains(res, self.maintenance.description)
        self.assertContains(res, self.maintenance.department.name)
