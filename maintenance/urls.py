from django.urls import path

from maintenance.views import (
    index,
    DepartmentListView,
    PositionListView,
    WorkerListView,
    MaintenanceListView,
    # DepartmentDetailView,
    # PositionDetailView,
    WorkerDetailView,
    MaintenanceDetailView,
    MaintenanceCreateView,
    MaintenanceUpdateView,
    MaintenanceDeleteView,
    SolasView,
    MarpolView,
    MlcView,
    ColregView,
)

urlpatterns = [
    path("", index, name="index"),
    path("solas/", SolasView.as_view(), name="solas"),
    path("marpol/", MarpolView.as_view(), name="marpol"),
    path("mlc/", MlcView.as_view(), name="mlc"),
    path("colreg/", ColregView.as_view(), name="colreg"),
    path("departments/", DepartmentListView.as_view(), name="department-list"),
    # path("departments/<int:pk>", DepartmentDetailView.as_view(), name="department-detail"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    # path("positions/<int:pk>", PositionDetailView.as_view(), name="position-detail"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>", WorkerDetailView.as_view(), name="worker-detail"),
    path("maintenance/", MaintenanceListView.as_view(), name="maintenance-list"),
    path("maintenance/<int:pk>", MaintenanceDetailView.as_view(), name="maintenance-detail"),
    path("maintenance/create", MaintenanceCreateView.as_view(), name="maintenance-create"),
    path("maintenance/update/<int:pk>", MaintenanceUpdateView.as_view(), name="maintenance-update"),
    path("maintenance/delete/<int:pk>", MaintenanceDeleteView.as_view(), name="maintenance-delete"),
]

app_name = "maintenance"
