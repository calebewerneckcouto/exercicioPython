import flet as ft



def main(page: ft.Page):
    
    page.title = "Minha Aplicação Flet"

    layout = ft.Column(
        controls=[
            ft.Text("Janela Principal",size=20,weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Botão1",on_click=lambda _:page.add(ft.Text("Botão 1 Clicado"))),
            ft.ElevatedButton("Botão2",on_click=lambda _:page.add(ft.Text("Botão 2 Clicado"))),
            ft.ElevatedButton("Botão3",on_click=lambda _:page.add(ft.Text("Botão 3 Clicado")))
        ]
    )

    page.add(layout)

ft.app(target=main)