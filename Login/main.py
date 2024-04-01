from flet import *
import flet as ft

def main(page: Page):
    page.title = "Login and Register",
    

    # Definir el tema de la pagina
    page.theme_mode = ThemeMode.DARK
    

    # Definir la estructura del contenedor de inicio de sesión
    login_container = Container(
        width=320,
        height=750,
        bgcolor="#ffffff",
        border_radius=10,
        content=Column(
            width=320,
            controls=[
                Container(
                    width=300,
                    margin=margin.only(left=170, right=20, top=5),  # Corregido el margen
                    content=TextButton(
                        "Create Account",
                        style=ButtonStyle(color="000000")
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=110, right=20, top=5),  # Corregido el margen
                    content=Text(
                        "Login",
                        size=30,
                        color="#000000",
                        weight='w700'
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=5),
                    alignment=alignment.center,
                    content=Text(
                        "Please enter your information below in order to login to your",
                        size=14,
                        color="#000000",
                        text_align="center"
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=5),
                    content=Column(
                        controls=[
                            Text(
                                "Username",
                                size=14,
                                color="#000000",
                            ),
                            TextField(
                                text_style=TextStyle(
                                    color="#000000",
                                ),
                                border_radius=15,
                                border_color=colors.BLACK,
                                focused_border_color=colors.ORANGE_700,
                            )
                        ]
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=5),
                    content=Column(
                        controls=[
                            Text(
                                "Password",
                                size=14,
                                color="#000000",
                            ),
                            TextField(
                                text_style=TextStyle(
                                    color="#000000",
                                ),
                                password=True,
                                can_reveal_password=True,
                                border_radius=15,
                                border_color=colors.BLACK,
                                focused_border_color=colors.ORANGE_700,
                            )
                        ]
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=5),  # Corregido el margen
                    content=TextButton(
                        "Forgot Password?",
                        style=ButtonStyle(color="#000000")
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=20),  # Corregido el margen
                    content=ElevatedButton(
                        "Login",
                        width=300,
                        height=55,
                        style=ButtonStyle(
                            bgcolor=colors.ORANGE_700,
                            color=colors.WHITE,
                            shape={
                                MaterialState.HOVERED: RoundedRectangleBorder(),
                                MaterialState.DEFAULT: RoundedRectangleBorder(),
                            },
                            padding=20,
                        )
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=15),  # Corregido el margen
                    content=Text(
                        "Or use social media account for login",
                        size=14,
                        text_align="center",
                        color="#000000",  # Corregido el color
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=10, right=10, top=5),  # Corregido el margen
                    content=Row(
                        controls=[
                            Container(
                                Image(
                                    r"assets/facebook.png",
                                    width=50,
                                ),
                                margin=margin.only(left=10),
                                on_click=lambda _: print("Google")
                            ),
                            Container(
                                Image(
                                    r"assets/gmail.png",  # Corregido el nombre del archivo de imagen
                                    width=50,
                                ),
                                margin=margin.only(left=10),
                                on_click=lambda _: print("Google")
                            ),
                            Container(
                                Image(
                                    r"assets/google.png",  # Corregido el nombre del archivo de imagen
                                    width=50,
                                ),
                                margin=margin.only(left=10),
                                on_click=lambda _: print("Google")
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    )
                )
            ]
        ),
    )

    # Definir la estructura del contenedor de registro
    signup_container = Container(
        width=320,
        height=750,
        bgcolor="#ffffff",
        border_radius=10,
        content=Column(
            width=320,
            controls=[
                Container(
                    width=48,
                    height=48,
                    border_radius=10,
                    margin=margin.only(left=20, right=20, top=10),
                    content=IconButton(
                        icon_color="#000000",
                        icon=icons.ARROW_BACK_IOS_NEW_OUTLINED,
                        style=ButtonStyle(
                         side={
                                MaterialState.DEFAULT:border.BorderSide(1, colors.BLACK26)
                            },
                        )
                    )
                )
            ]
        )  # Aquí deberías añadir el contenido del contenedor de registro
    )

    # Crear el cuerpo de la página
    body = Container(
        width=1000,
        height=800,
        content=Row(
            controls=[
                login_container,
                signup_container
            ]
        )
    )

    # Agregar el cuerpo a la página
    page.add(body)


app(main,  view=ft.WEB_BROWSER);