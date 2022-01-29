# Add your Views Here
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task


def task_view(request):
    search_term = request.GET.get("search")
    tasks = Task.objects.filter(completed=False).filter(deleted=False)
    if search_term:
        tasks = tasks.filter(title__icontains=search_term)
    return render(request, "tasks.html", {"tasks": tasks})


def add_task_view(request):
    task_string = request.GET.get("task")
    Task(title=task_string).save()
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, id):
    # soft delete task
    Task.objects.filter(id=id).update(deleted=True)
    return HttpResponseRedirect("/tasks")


def complete_task(request, id):
    # marking task as completed
    Task.objects.filter(id=id).update(completed=True)
    return HttpResponseRedirect("/tasks")


def completed_task_view(request):
    completed_tasks = Task.objects.filter(completed=True).filter(deleted=False)
    return render(request, "completed_tasks.html", {"tasks": completed_tasks})