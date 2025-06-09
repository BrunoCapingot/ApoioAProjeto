from django.shortcuts import render, redirect
from appRodrigo.models import Usuario, CadastroDeUsuario, Refatoracao

def index(request):
    if request.method == 'POST':
        erro_bool = False
        user_bool = False
        pass_bool = False
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        dict_templates = dict()
        usuarios_do_banco = Usuario.objects.values_list('usuario','senha','categoria')
        for usuario_cadastrado in usuarios_do_banco:
            usuario = usuario_cadastrado[0]
            senha = usuario_cadastrado[1]
            categoria = usuario_cadastrado[2]
            if username_input == usuario:
                user_bool = True
            if password_input == senha:
                pass_bool = True
            if user_bool == True and pass_bool == True:
                erro_bool = True
                request.session['usuario'] = usuario
                request.session['categoria'] = categoria
                dict_templates = {'1':'template_gerente','2':'template_tester','3':'template_desenvolvedor'}
                break
        if erro_bool == True:
            return redirect(dict_templates[categoria])
        else:
            return render(request, 'index.html', {'erro': 'aa'})

    return render(request, 'index.html')

def template_gerente(request):
    if request.method == 'POST':

        if request.POST.get('formulario') == 'cadastro_refatoracao':
            projeto = request.POST.get('ref-projeto')
            titulo = request.POST.get('ref-titulo')
            descricao = request.POST.get('ref-descricao')
            atribuicao = request.POST.get('ref-equipe')
            nova_refatoracao = Refatoracao(projeto=projeto,equipe=atribuicao,descricao=descricao,titulo=titulo)
            nova_refatoracao.save()

        if request.POST.get('formulario') == 'cadastro_usuarios':
            cad_nome_usuario = request.POST.get('usr-nome')
            cad_equipe_usuario = request.POST.get('usr-equipe')
            cad_email_usuario = request.POST.get('usr-email')
            cad_senha_usuario = request.POST.get('usr-senha')
            novo_usuario = CadastroDeUsuario(usuario=cad_nome_usuario,equipe=cad_equipe_usuario,email=cad_email_usuario,senha=cad_senha_usuario)
            novo_usuario.save()
            return render(request, 'Gerente.html', {'mensagem': 'Usuário cadastrado com sucesso!'})
    usuarios_do_banco = Usuario.objects.values_list('usuario', 'senha', 'categoria')
    print(usuarios_do_banco)
    return render(request, 'Gerente.html', {'usuarios_cadastrados':usuarios_do_banco})
