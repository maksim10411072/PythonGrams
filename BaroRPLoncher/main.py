import builtins
import os
import flet as ft
import minecraft_launcher_lib as mcl
# Много мне нужно тут понакодить...
# Короче, я решил так: внутри def main() я буду писать все, что связано с юзер-интерфейсом, а все функции скачивания, установки и прочего будут вне функции, но в этом же файле.
# Получается такая однофайловая ультрамакаронная система.

minecraft_directory = "/minecraft"


def main(page: ft.Page):
    # Пока что закомментировал, по нужде раскомментировать и, если нужно, изменить
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "BaroRPLoncher"
    PlayerName = ft.TextField(label="Никнейм")
    LogTextControl = ft.Text('Великие начала начинаются с великих концов.\n')
    
    # Это решение мне предложила нейросеть. Они умнеют!
    def customloggingprint(*args, **kwargs):
        log_text = LogTextControl.value + ' '.join(map(str, args)) + '\n'
        LogTextControl.value = log_text
        page.update()
        builtins.print(*args, **kwargs)
    print = customloggingprint

    def on_play_click(e):
        print("Нерабочий лаунчер, ноутбук в дыму")
    def on_install_click(e):
        print("Что творит Максимка не понять уму!")
    page.add(
        ft.SafeArea(
            ft.Column(
                [

                    ft.Tabs(
                    [
                        ft.Tab(text="Лог", content=ft.Container(
                            # ft.Image(src="/assets/no_x.jpg", fit=ft.ImageFit.CONTAIN, width=900, height=900), 
                            # alignment=ft.alignment.center
                            # Картинки не работаеют. No images?
                            LogTextControl
                            )
                        )
                    ],
                    is_secondary=True,
                    expand=1
                    ),

                    ft.Row(
                    [
                        PlayerName,
                        ft.FilledButton("Играть", on_click=on_play_click),
                        ft.FilledButton("Установить", on_click=on_install_click)
                    ]
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            expand=1
        )
    )

        


ft.app(main)
