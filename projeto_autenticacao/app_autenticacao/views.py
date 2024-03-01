from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario

#login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            usuario = Usuario.objects.get(username=username)
            if check_password(password, usuario.password):
                print('Login efetuado com sucesso')
                return render(request, 'home/home.html', {'usuario': usuario})
            else:
                print('Senha incorreta')
                return render(request, 'login/login.html', {'erro': 'Senha incorreta'})
        except Usuario.DoesNotExist:
            print('Usuário não encontrado')
            return render(request, 'registration/register.html', {'erro': 'Usuário não encontrado'})
    else:
        return render(request, 'login/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Validar se o usuário já existe
        if Usuario.objects.filter(username=username).exists():
            return render(request, 'registration/register.html', {'erro': 'Nome de usuário já está em uso'})
        # Criar o novo usuário
        novo_usuario = Usuario(username=username, email=email, password=make_password(password))
        novo_usuario.save()
        return render(request, 'registration/register.html', {'cadastro_sucesso': True})
    else:
        return render(request, 'registration/register.html')
