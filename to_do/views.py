from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

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
                
            return redirect('/home') 
    except Exception as ec:
        print(ec)
        return redirect('')        
    
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
                return render(request, 'home.html',{
                    'user_name': user.get_username()
                    })
        return render(request, 'sigin.html',{
            'error': 'Usuario o contraseña invalidos'
        })
    except Exception as ec:
        print(ec)
        return redirect('/')
    
def landing(request):
    return render(request, 'index.html')
    
def home(request):
    return render(request,'home.html' )

def close_sesion(request):
    logout(request)
    return redirect('/')