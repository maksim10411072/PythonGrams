import flet as ft
import minecraft_launcher_lib as mcl
# Много мне нужно тут понакодить...

def main(page: ft.Page):
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Text("Привет, мир!"),
                    ft.ElevatedButton("Нажми меня!", on_click=lambda _: page.update())
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
    )


ft.app(main)
