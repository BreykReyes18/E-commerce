import flet as ft

conteiner = ft.Container(
    ft.Column([
        ft.Container(
            ft.Text(
                "Login",
                width=320,
                size=30,
                text_align="center",
                weight="w900",
            ),
            padding= ft.padding.only(20,20),
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Email",
                border="underline",
                color="black",
                prefix_icon=ft.icons.EMAIL
            ),
            padding= ft.padding.only(20,20),
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Password",
                border="underline",
                color="black",
                prefix_icon=ft.icons.LOCK,
                password=True
            ),
            padding= ft.padding.only(20,20),
        ),

        ft.Container(
            ft.Checkbox(
                label="Remember me",
                check_color= "black",
            ),
            padding= ft.padding.only(20,20),
        ),
        ft.Container(
            ft.ElevatedButton(
                text="Login",
                width=280,
                bgcolor="black"
            ),
            padding= ft.padding.only(20,20),
        ),
        ft.Text("Login with",
                text_align="center",
                width=320),

        ft.Container(
            ft.Row([
                ft.IconButton(
                    icon=ft.icons.EMAIL,
                    tooltip="Google",
                    icon_size="35"
                ),
                ft.IconButton(
                    icon=ft.icons.FACEBOOK,
                    tooltip="Facebook",
                    icon_size="35"
                ),
                ft.IconButton(
                    icon=ft.icons.APPLE,
                    tooltip="Apple",
                    icon_size="35"
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
            padding= ft.padding.only(20,20),
        ),
        ft.Container(
            ft.Row([
                ft.Text("Don't have an account?"),
                ft.TextButton(
                    text="Sign up"),
                ft.Text("Brandon")
            ])
        )
    ],
    alignment=ft.MainAxisAlignment.SPACE_EVENLY
    ),

    border_radius=20,
    width=320,
    height=500,
    gradient= ft.LinearGradient([
        ft.colors.PURPLE,
        ft.colors.PINK,
        ft.colors.RED
    ])
)

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(conteiner)
    pass

ft.app(main, view=ft.WEB_BROWSER)
