import flet as ft



def main(page: ft.Page):
    
    page.title = "Estilização Básica"

    page.add(
    ft.Text("Texto com cor Verde",color="blue",size=20),
    ft.ElevatedButton("Clique Aqui!", color="white",bgcolor="green",   on_click=lambda _:page.add(ft.Text("Botão Verde Clicado"))),
    ft.Text("Texto com cor Vermelha",color="blue",size=25),
    ft.ElevatedButton("Clique Aqui!", color="white",bgcolor="red",   on_click=lambda _:page.add(ft.Text("Botão Vermelho Clicado")))



    )

ft.app(target=main)