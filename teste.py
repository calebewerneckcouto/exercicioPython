import flet as ft


nome = "Calebe"
idade = 36
   


def main(page: ft.Page):
    
    ola = ft.Text(value=f'Olá {nome} vc tem {idade} anos',size=30)    
    page.controls.append(ola)
    page.update()

ft.app(target=main)