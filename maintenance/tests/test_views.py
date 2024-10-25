from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from maintenance.models import Maintenance, Department, Position, Worker
from maintenance.forms import MaintenanceForm

class PublicMaintenanceTest(TestCase):
    def setUp(self):
        self.url_create = reverse("maintenance:maintenance-create")
        self.url_update = reverse("maintenance:maintenance-update", kwargs={"pk": 1})
        self.url_delete = reverse("maintenance:maintenance-delete", kwargs={"pk": 1})

    def test_login_required_create(self):
        res = self.client.get(self.url_create)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_update(self):
        res = self.client.get(self.url_update)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_delete(self):
        res = self.client.get(self.url_delete)
        self.assertNotEqual(res.status_code, 200)


class PrivateMaintenanceTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)
        self.department = Department.objects.create(name="Test Department")
        self.position = Position.objects.create(name="Test Position")
        self.worker = Worker.objects.create_user(
            username="worker",
            password="testworker",
            position=self.position
        )
        self.maintenance = Maintenance.objects.create(
            name="Ecdis",
            description="Test description 1",
            deadline=timezone.now().date(),
            is_completed=False,
            department=self.department
        )
        self.url_list = reverse("maintenance:maintenance-list")
        self.url_create = reverse("maintenance:maintenance-create")
        self.url_update = reverse("maintenance:maintenance-update", kwargs={"pk": self.maintenance.pk})
        self.url_delete = reverse("maintenance:maintenance-delete", kwargs={"pk": self.maintenance.pk})

    def test_retrieve_maintenances(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ecdis")
        maintenances = Maintenance.objects.all()
        self.assertEqual(
            list(response.context["maintenance_list"]),
            list(maintenances)
        )
        self.assertTemplateUsed(response, "maintenance/maintenance_list.html")

    def test_create_maintenance(self):
        data = {
            "name": "Test Maintenance",
            "description": "Test description",
            "deadline": timezone.now().date(),
            "is_completed": False,
            "department": self.department.pk,
            "person_in_charge": [self.worker.pk],
        }
        response = self.client.post(self.url_create, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Maintenance.objects.filter(name="Test Maintenance").exists())

    def test_search_maintenance(self):
        Maintenance.objects.create(
            name="inmarsat-c",
            description="Test description 2",
            deadline=timezone.now().date(),
            is_completed=False,
            department=self.department
        )
        response = self.client.get(self.url_list, {"name": "Ecdis"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ecdis")
        self.assertNotContains(response, "inmarsat-c")
