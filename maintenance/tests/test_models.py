from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from maintenance.models import Department, Position, Maintenance


class ModelsTests(TestCase):
    # checks __str__ in Department
    def test_department_str(self):
        department = Department.objects.create(name="test")
        self.assertEqual(str(department), department.name)

    # checks __str__ in Position
    def test_position_str(self):
        position = Position.objects.create(name="test")
        self.assertEqual(str(position), position.name)

    # checks __str__ in Worker
    def test_worker_str(self):
        position = Position.objects.create(name="test")
        worker = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
            position=position,
        )
        self.assertEqual(
            str(worker),
            f"{worker.username} ({worker.first_name} {worker.last_name} {worker.position.name})"
        )

    # checks creation Maintenance instance and its relations many to many with Worker
    def test_maintenance(self):
        department = Department.objects.create(name="Test Department")
        position = Position.objects.create(name="Test Position")

        worker1 = get_user_model().objects.create(
            username="worker1",
            password="test123",
            first_name="Worker",
            last_name="One",
            position=position,
        )

        worker2 = get_user_model().objects.create(
            username="worker2",
            password="test123",
            first_name="Worker",
            last_name="Two",
            position=position,
        )

        maintenance = Maintenance.objects.create(
            name="Test Maintenance",
            description="Test description",
            deadline=date.today(),
            is_completed=True,
            department=department,
        )

        maintenance.person_in_charge.set([worker1, worker2])
        maintenance.save()

        self.assertIn(worker1, maintenance.person_in_charge.all())
        self.assertIn(worker2, maintenance.person_in_charge.all())

    # checks creation Worker`s instance with field position
    def test_create_worker_with_position(self):
        username = "test"
        password = "test123"
        position = Position.objects.create(name="Test Position")
        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            position=position,
        )
        self.assertEqual(worker.username, username)
        self.assertEqual(worker.position, position)
        self.assertTrue(worker.check_password(password))
