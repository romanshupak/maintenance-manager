from django.test import TestCase
from django.utils import timezone
from maintenance.forms import MaintenanceForm
from maintenance.models import Department, Position, Worker


class MaintenanceFormTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Test Department")
        self.position = Position.objects.create(name="Test Position")
        self.worker = Worker.objects.create_user(
            username="worker",
            password="testworker",
            position=self.position
        )

    def test_form_has_fields(self):
        form = MaintenanceForm()
        expected_fields = ['name', 'description', 'deadline', 'is_completed', 'department', 'person_in_charge']
        actual_fields = list(form.fields)
        self.assertCountEqual(actual_fields, expected_fields)

    def test_form_valid_data(self):
        data = {
            'name': 'Test Maintenance',
            'description': 'Test description',
            'deadline': timezone.now().date(),
            'is_completed': False,
            'department': self.department.pk,
            'person_in_charge': [self.worker.pk]
        }
        form = MaintenanceForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        data = {
            'name': '',
            'description': 'Test description',
            'deadline': 'invalid-date',
            'is_completed': False,
            'department': self.department.pk,
            'person_in_charge': [self.worker.pk]
        }
        form = MaintenanceForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('deadline', form.errors)
