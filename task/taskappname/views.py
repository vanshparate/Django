from django.shortcuts import render


def task_view(request):
    tasks = [
        {'id': 1, 'title': 'Task 1'},
        {'id': 2, 'title': 'Task 2'},
        {'id': 3, 'title': 'Task 3'},
    ]

    return render(request, 'task.html', {'tasks': tasks})
    # return render(request, 'task.html')
