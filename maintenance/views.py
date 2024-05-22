from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from maintenance.forms import MaintenanceForm
from maintenance.models import Department, Position, Worker, Maintenance


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_departments = Department.objects.count()
    num_positions = Position.objects.count()
    num_workers = Worker.objects.count()
    num_completed_maintenances = Maintenance.objects.filter(is_completed=True).count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_departments": num_departments,
        "num_positions": num_positions,
        "num_workers": num_workers,
        "num_completed_maintenances": num_completed_maintenances,
        "num_visits": request.session["num_visits"]
    }
    return render(request, "maintenance/index.html", context=context)


class DepartmentListView(LoginRequiredMixin, generic.ListView):
    model = Department
    template_name = "maintenance/department_list.html"
    context_object_name = "department_list"
    queryset = Department.objects.order_by("name")


class DepartmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Department
    template_name = "maintenance/department_detail.html"
    context_object_name = "department_detail_list"


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "maintenance/position_list.html"
    context_object_name = "position_list"


class PositionDetailView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "maintenance/position_detail.html"
    context_object_name = "position_detail_list"
    paginate_by = 3


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "maintenance/worker_list.html"
    context_object_name = "worker_list"
    queryset = Worker.objects.select_related("position")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "maintenance/worker_detail.html"
    context_object_name = "worker_detail_list"


class MaintenanceListView(LoginRequiredMixin, generic.ListView):
    model = Maintenance
    template_name = "maintenance/maintenance_list.html"
    context_object_name = "maintenance_list"
    queryset = (
        Maintenance.objects
        .select_related("department")
        .prefetch_related("person_in_charge")
    )


class MaintenanceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Maintenance
    # fields = "__all__"
    success_url = reverse_lazy("maintenance:maintenance-list")
    template_name = "maintenance/maintenance_create.html"
    form_class = MaintenanceForm


class MaintenanceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Maintenance
    template_name = "maintenance/maintenance_detail.html"
    context_object_name = "maintenance_detail_list"


class MaintenanceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Maintenance
    # fields = "__all__"
    success_url = reverse_lazy("maintenance:maintenance-list")
    template_name = "maintenance/maintenance_form.html"
    form_class = MaintenanceForm


class MaintenanceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Maintenance
    template_name = "maintenance/maintenance_form_confirm_delete.html"
    success_url = reverse_lazy("maintenance:maintenance-list")

