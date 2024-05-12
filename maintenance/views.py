from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from maintenance.models import Department, Position, Worker, Maintenance


def index(request: HttpRequest) -> HttpResponse:
    num_departments = Department.objects.count()
    num_positions = Position.objects.count()
    num_workers = Worker.objects.count()
    num_completed_maintenances = Maintenance.objects.filter(is_completed=True).count()
    context = {
        "num_departments": num_departments,
        "num_positions": num_positions,
        "num_workers": num_workers,
        "num_completed_maintenances": num_completed_maintenances,
    }
    return render(request, "maintenance/index.html", context=context)


class DepartmentListView(generic.ListView):
    model = Department
    template_name = "maintenance/department_list.html"
    context_object_name = "department_list"


class PositionListView(generic.ListView):
    model = Position
    template_name = "maintenance/position_list.html"
    context_object_name = "position_list"


class WorkerListView(generic.ListView):
    model = Worker
    template_name = "maintenance/worker_list.html"
    context_object_name = "worker_list"


class MaintenanceListView(generic.ListView):
    model = Maintenance
    template_name = "maintenance/maintenance_list.html"
    context_object_name = "maintenance_list"
