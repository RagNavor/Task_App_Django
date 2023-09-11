from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Project, Task
from datetime import datetime

# Create your views here.


#GET
def singup(request):
    try: 
        ''' If request method is GET return a page with form to signup  '''
        if request.method == 'GET':
            return render(request,'singup.html')
    except Exception as ec:
        print(ec)
        return redirect('/')
    try:
        ''' If the request method is POST, the following parameters are expected to be received: Nombre, Apellido, Correo, password1 and password2. With these parameters, the user will be created. If successful, the session will be started and the user will be redirected to the home page
    
        Parameters:
            Nombre (str): name
            Apellido (str): lastname
            Correo (str): email
            password1 (str): password
            password2 (str): password  '''
            
        if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(username = request.POST['Correo'], first_name = request.POST['Nombre'] ,last_name = request.POST['Apellido'] ,email = request.POST['Correo'],password= request.POST['password1'] )
                user.save()
                
                
                login(request, user)
                return redirect('home')
            else:
                
                return render(request,'singup.html',{
                'error': 'Las contraseñas no coinciden, por favor verifique'
            }) 
    except Exception as ec:
        print(ec)
        return redirect('/')        
    
def sigin(request):
    try:
        if request.method == 'GET':
            return render(request, 'sigin.html')
            
    except Exception as ec:
        print(ec)
        return redirect('/')
    try:
        if request.method == 'POST':
            user = authenticate(request, username = request.POST['Correo'], password= request.POST['Contraseña'] )
            print(user)
            print(request)
            if user != None:
                print(user)
                login(request, user)
                return redirect('home')
            '''{
                    'user_name': user.get_username()
                    })'''
        return render(request, 'sigin.html',{
            'error': 'Usuario o contraseña invalidos'
        })
    except Exception as ec:
        print(ec)
        return redirect('/')
    
def landing(request):
    return render(request, 'index.html')
    
def home(request):
    projects_tasks = []
    task_completed = []
    print(request.user.first_name)
    projects = Project.objects.filter(created_by_user_id= request.user)
    for project in projects:
        projects_tasks.append((project,Task.objects.filter(project_id=project), Task.objects.filter(project_id=project, estado='Completado')))
    print(projects)
    print(projects_tasks)
    return render(request, 'home.html',{
        'projects_tasks':projects_tasks
    })
    
def close_sesion(request):
    logout(request)
    return redirect('/')

def project(request):
    projects_tasks = []
    task_completed = []
    projects_in_development= []
    projects_completed = []
    projects_discarded =[]
    print(request.user.first_name)
    projects = Project.objects.filter(created_by_user_id= request.user)
    
    for project in projects:
        projects_tasks.append((project,Task.objects.filter(project_id=project), Task.objects.filter(project_id=project, estado='Completado')))
    for project_tasks in projects_tasks:
        print(project_tasks[0].estado)
        if project_tasks[0].estado == 'En desarrollo' or project_tasks[0].estado == 'En Desarrollo':
            projects_in_development.append(project_tasks)
        if project_tasks[0].estado == 'Completado':
            projects_completed.append(project_tasks)
        if project_tasks[0].estado == 'Descartado':
            projects_discarded.append(project_tasks)
    
    print(projects_in_development)
    dead_line_min= str(datetime.now())
    return render(request, 'projects.html',
                  {'projects_in_development': projects_in_development,
                  'projects_completed':projects_completed,
                  'projects_discarded':projects_discarded,
                   'dead_line_min':dead_line_min,
                   'projects_tasks':projects_tasks
                   }
                  )

def detail_project(request,id):
    try: 
        
        project = Project.objects.get(pk = id)
        tasks = Task.objects.filter(project_id=project.pk)
        dead_line_min= str(datetime.now())
        return render(request, 'project_detail.html',{
            'project':project,
            'id_project':project.pk,
            'dead_line_min':dead_line_min,
            'tasks': tasks
        })
    except Exception as ec:
        print(ec)
        
#POST


    
#projects

def create_project(request):
    try:
        project = Project.objects.create(
            name =request.POST['nombre_proyecto'],
            description = request.POST['descrpcion_proyecto'],
            dead_line = request.POST['entrega_proyecto'], 
            estado = 'En Desarrollo',
            created_by_user_id = request.user)
        project.save()
        return redirect('project')
    except KeyError as ke:
        print(request.POST['entrega_proyecto'])
        print(ke)
        
    except Exception as ec:
        print(ec)
        print(request.POST['entrega_proyecto'])
        return redirect('project')
    
def update_project(request,id):
    pass
def delete_project(request,id):
    project = Project.objects.filter(pk = id).delete()
    return redirect('project')
    
    
    
#tasks 
def create_task(request,id):
    try:
        project = Project.objects.get(pk = id)
        print(project)
        task = Task.objects.create(
            name = request.POST['Nombre'],
            description = request.POST['descripcion'], 
            project_id = project,
            dead_line =request.POST['Fecha_de_culminacion'] )
        task.save()
        return redirect(f'/detail_project/{id}')
    except Exception as ec:
        print(ec)
        print(id)
        print(project)
        return redirect(f'/detail_project/{id}')
def update_task(request):
    pass
def delete_task(request, id):
    
    pass