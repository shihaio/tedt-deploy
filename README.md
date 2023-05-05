DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Past failed codes:
Views
# def ViewUserTask(request, pk):
#     pic= User.objects.filter(id=1).first()
#     tasksOfPIC = pic.tasks_assignedto.all()
#     print("========================> tasksOfPIC", tasksOfPIC)	
#     task = Task.objects.filter(tasked_to_id=pk)
#     #print("========================>", task)
#     tasks= task.values('id', 'task_name', 'status','description','taskImgURL','created_by_id','tasked_to_id')
#     view_list = list(tasks)
#     #print("========================>", view_list)
#     return JsonResponse(view_list, safe=False)

# def ViewUserTask(request, pk):

#     pic= User.objects.filter(id=1).first()
#     tasksOfPIC = pic.tasks_assignedto.all()
#     print("========================> tasksOfPIC", tasksOfPIC)	
#     print("========================>", pk)

#     task = Task.objects.filter(tasked_to_id=pk)
#     #print("========================>", task)
#     tasks= tasksOfPIC.values('id', 'task_name', 'status','description','taskImgURL','created_by_id','tasked_to_id')
#     view_list = list(tasks)
#     #print("========================>", view_list)
#     return JsonResponse(view_list, safe=False)