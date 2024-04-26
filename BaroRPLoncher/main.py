import builtins
import os
import flet as ft
import minecraft_launcher_lib as mcl
import subprocess
# Много мне нужно тут понакодить...
# Короче, я хотел писать все прочие функции вне main(), но не удалось :(
username = "test"

normal_minecraft_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "minecraft")
def percentage(a, b, as_str=False):
    try:
        result = b/a * 100
        if as_str:
            return str(round(result)) + "%"
    except ZeroDivisionError:
        result = "0"
    result

def main(page: ft.Page):
    # Пока что закомментировал, по нужде раскомментировать и, если нужно, изменить
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "BaroRPLoncher"

    def define_username(e):
        eventoutput = e.control.value
        print(eventoutput)
        global username
        username = eventoutput
        print(username)

    PlayerName = ft.TextField(label="Никнейм", on_change=define_username)
    LogTextControl = ft.Text('Великие начала начинаются с великих концов.\n')
    
    # Это решение мне предложила нейросеть. Они умнеют!
    def customloggingprint(*args, **kwargs):
        log_text = LogTextControl.value + ' '.join(map(str, args)) + '\n'
        LogTextControl.value = log_text
        LogTextControl.update()
        builtins.print(*args, **kwargs)
    print = customloggingprint

    # Функции, которые будут вызываться в процессе закачки и всякое такое

    def statusPrint(*args, **kwargs):
        print("Операция:", *args, **kwargs)
    def progressPrint(*args):
        print("Прогресс:", args[0], "/", CallbackMaxOutput, "в процентах:", percentage(CallbackMaxOutput, args[0], True))
    def maxPrint(*args):
        global CallbackMaxOutput
        CallbackMaxOutput = args[0]
        print("Всего нужно:", CallbackMaxOutput)

    standart_callback = {
        "setStatus": statusPrint,
        "setProgress": progressPrint,
        "setMax": maxPrint
    }

    # Функция закачки майнкрафта. Тут по идее будет проверка, закачка и всё такое
    def installation_function(callback):
        # Каким-то магическим образом майнкрафт оказывается установлён хотя там его буквально нет.
        # minecraft_installed = mcl.utils.is_minecraft_installed(normal_minecraft_directory)
        # if normal_minecraft_directory:
        #     print("Майнкрафт уже установлен!")
        #     print(normal_minecraft_directory)
        # if not normal_minecraft_directory:
        print("Качаем майнкрафт...")
        print("Осторожно! Может ОЧЕНЬ сильно лагать!")
        mcl.install.install_minecraft_version("1.19.2", normal_minecraft_directory, callback)
        print("Закачка удачна!")

    def run_minecraft():
        standart_options = {
            # This is needed
            "username": username,
            "uuid": username,
            "token": "",
            # This is optional
            "launcherName": "BaroRPLoncher", # The name of your launcher
        }
        command = mcl.command.get_minecraft_command("1.19.2", normal_minecraft_directory, options=standart_options)
        print("Огромные стартовые аргументы:")
        print(command)
        print("Запускаем майнкрафт...")
        subprocess.run(command)

    def on_play_click(e):
        print("Нерабочий лаунчер, ноутбук в дыму")
        run_minecraft()
    def on_install_click(e):
        print("Что творит Максимка не понять уму!")
        installation_function(standart_callback)

    
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
                            ft.Column([LogTextControl], scroll=ft.ScrollMode.ADAPTIVE, auto_scroll=True)
                            )
                        )
                    ],
                    is_secondary=True,
                    expand = 1
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

        
print("hm???")

ft.app(main)
