import flet as ft

def main(page: ft.Page):
    btn = ft.Button(
        text="Clique Aqui",
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        border_radius=8,
    )
    page.add(btn)

ft.app(target=main)    