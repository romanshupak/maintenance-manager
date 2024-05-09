from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from maintenance.models import Department, Position, Worker, Maintenance


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["name"]


@admin.register(Position)
class Position(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["name"]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("position", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("position", )}),)


@admin.register(Maintenance)
class Maintenance(admin.ModelAdmin):
    list_display = [
        "name", "description",
        "deadline", "is_completed",
        "department",
    ]
    search_fields = ["name", ]
    list_filter = ["department", ]

