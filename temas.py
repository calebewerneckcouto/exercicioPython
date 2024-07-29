import flet as ft

def main(page: ft.Page):
    theme = ft.Theme(
        color_scheme = ft.ColorScheme(
            prymary=ft.colors.BLUE,
            secondary=ft.colors.GREEN,
            background=ft.colors.WHITE,
            surface=ft.colors.GREY,
            on_primary=ft.colors.WHITE,
            on_secondary=ft.colors.WHITE,
            on_background=ft.colors.WHITE,
            on_surface=ft.colors.BLACK,

        )
    )

    page.theme = theme   
 
    page.add(
        ft.Text("Texto com cor Verde",color="blue",size=20),
        ft.ElevatedButton("Clique Aqui!", color="white",bgcolor="green",   on_click=lambda _:page.add(ft.Text("Botão Verde Clicado"))),
        ft.Text("Texto com cor Vermelha",color="blue",size=25),
        ft.ElevatedButton("Clique Aqui!", color="white",bgcolor="red",   on_click=lambda _:page.add(ft.Text("Botão Vermelho Clicado"))),
    )

ft.app(target=main)