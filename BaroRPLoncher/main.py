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
    def on_play_click(e):
        pass #Надо сделать
    def on_install_click(e):
        pass #Надо сделать
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Image(f"/assets/no_x.png", height=100, width=100, fit=ft.ImageFit.NONE, repeat=ft.ImageRepeat.NO_REPEAT),
                    # Я хз почему, но эта херня отказывается работать. Для баланса вселенной я оставил вверху картинку no logs? чтобы она напоминала мне о том что мне нужно сделать
                    # UPD: Да тут картинки вообще не работают!
                    # Оказывается что это похоже не у меня одного проблема, ждём пока исправят

                    # ft.Tabs([
                    #     ft.Tab(text="Лог", content=ft.Container(
                    #         ft.Image(src="/assets/no_x.jpg", fit=ft.ImageFit.CONTAIN, width=900, height=900), 
                    #         alignment=ft.alignment.center
                    #         )
                    #     )
                    # ],
                    # is_secondary=True,
                    # expand=1
                    # ),

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
