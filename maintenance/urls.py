from django.urls import path

from maintenance.views import (
    index,
    DepartmentListView,
    PositionListView,
    WorkerListView,
    MaintenanceListView,
    DepartmentDetailView,
    PositionDetailView,
    WorkerDetailView,
    MaintenanceDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("departments/", DepartmentListView.as_view(), name="department-list"),
    path("departments/<int:pk>", DepartmentDetailView.as_view(), name="department-detail"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>", PositionDetailView.as_view(), name="position-detail"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>", WorkerDetailView.as_view(), name="worker-detail"),
    path("maintenance/", MaintenanceListView.as_view(), name="maintenance-list"),
    path("maintenance/<int:pk>", MaintenanceDetailView.as_view(), name="maintenance-detail"),
]

app_name = "maintenance"
