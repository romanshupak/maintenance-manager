from django.urls import path

from maintenance.views import index, DepartmentListView, PositionListView

urlpatterns = [
    path("", index, name="index"),
    path("departments/", DepartmentListView.as_view(), name="department-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
]

app_name = "maintenance"
