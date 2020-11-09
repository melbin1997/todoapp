from django.shortcuts import render
from .models import TodoList
from collections import defaultdict
from django.views import View

class myView(View):

    def findChildren(self, values, newDict, s):
        m = ""
        for x in values:
            if x in newDict.keys():
                temp = TodoList.objects.get(id=x)
                m += '<li><h3 class="complete-{}">{}  <a href="?done&id={}">Done</a>  <a href="?delete&id={}">Delete</a></h3>'.format(temp.completed,str(temp),x,x)
                m += '<form action="" method="get"><input type="text" id="description" class="taskName" placeholder="What do you need to do?" name="description"><button class="taskAdd" name="taskAdd" type="submit"  id="{}" value="{}">Add task</button></form>'.format(x,x)
                m += "<ul>"
                m += self.findChildren(newDict[x], newDict,s)
                m += "</ul></li>"
            else:
                temp = TodoList.objects.get(id=x)
                m += '<li><h3 class="complete-{}"">{}  <a href="?done&id={}">Done</a>  <a href="?delete&id={}">Delete</a></h3>'.format(temp.completed, str(temp),x,x)
                m += '<form action="" method="get"><input type="text" id="description" class="taskName" placeholder="What do you need to do?" name="description"><button class="taskAdd" name="taskAdd" type="submit"  id="{}" value="{}">Add task</button></form>'.format(x,x)
                m += "</li>"
        return m 

    def get(self, request):
        print("Get request : ", request)
        if "clearAll" in request.GET:
            TodoList.objects.all().delete()
        if "taskAdd" in request.GET:
            title = request.GET["description"]
            parent = request.GET["taskAdd"]
            todo = TodoList(title = title, parent = parent)
            todo.save()
        if "done" in request.GET:
            id = request.GET["id"]
            todo = TodoList.objects.get(id=id)
            todo.completed=True
            todo.save()
        if "delete" in request.GET:
            id = request.GET["id"]
            todo = TodoList.objects.get(id=id)
            todo.delete()

        todos = TodoList.objects.all()

        newDict = defaultdict(lambda:[])
        childDict = {}
        for todo in todos:
            newDict[todo.parent].append(todo.id)

        s='<ul class = "taskList">' 
        s += self.findChildren(newDict[-1], newDict, s)
        s +="\n</ul>"
        return render(request, "index.html", {"newDict": newDict, "s": s})   

    

    
             