def main(page: ft.Page):
    container=ft.Container(
        content=ft.Text("Texto responsivo"),
        padding=ft.EdgeInsets.all(10),
        margin=ft.EdgeInsets.symmetric(vertical=5,horizonotal=20),
        width=page.width / 2,
        heigth=page.height / 4
    
    )
    page.add(container)

ft.app(target=main)

