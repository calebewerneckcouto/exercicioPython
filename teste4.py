import flet as ft



def main(page: ft.Page):
    
    page.title = "Minha Aplicação Flet"

    page.add(
        ft.Text("Bem Vindo ao Flet"),
        ft.ElevatedButton("Clique Aqui!",on_click=lambda _: page.add(ft.Text("Botão Clicado!")))

    )

    

ft.app(target=main)