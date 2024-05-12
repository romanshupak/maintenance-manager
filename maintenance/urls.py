from django.urls import path

from maintenance.views import (
    index,
    DepartmentListView,
    PositionListView,
    WorkerListView,
    MaintenanceListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("departments/", DepartmentListView.as_view(), name="department-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("maintenance/", MaintenanceListView.as_view(), name="maintenance-list"),
]

app_name = "maintenance"
