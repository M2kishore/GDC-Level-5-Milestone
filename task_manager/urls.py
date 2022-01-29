from django.contrib import admin
from django.urls import path

from tasks.views import (
    task_view,
    add_task_view,
    delete_task_view,
    completed_task_view,
    complete_task,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", task_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:id>/", delete_task_view),
    path("complete_task/<int:id>/", complete_task),
    path("completed_tasks/", completed_task_view),
]
