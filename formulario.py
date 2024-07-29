import flet as ft


 


def main(page: ft.Page):
    page.title="Formulario de Cadastro"
    login = ft.TextField(hint_text="Digite seu login")
    senha = ft.TextField(hint_text="Digite sua senha")
    nome = ft.TextField(hint_text="Digite seu nome")
    email = ft.TextField(hint_text="Digite seu Email")
    cpf = ft.TextField(hint_text="Digite seu CPF")
    dados = [nome,email,cpf,login,senha]
    
   
    page.controls.append(login)
    page.controls.append(senha)
    page.controls.append(nome)
    page.controls.append(email)
    page.controls.append(cpf)
    ft.ElevatedButton("Cadastrar",on_click=lambda _:page.add(ft.Text("Nome"))),
    page.update()

ft.app(target=main)