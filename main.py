import flet as ft
# renderiza a pagina do jogo
def main(page: ft.Page):
    page.title = "CardGame"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.bgcolor = "black"
    image = ft.Container(
        expand=2,
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, 1 ),
            end=ft.Alignment(1, -1),
            colors=["brown", "surface"]
        ),
        content=ft.Image(src='https://s3-us-west-2.amazonaws.com/s.cdpn.io/195612/barbarian.png',width=400,height=400,scale=ft.Scale(scale=1.6))
    )
    info = ft.Container(
        expand=2,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ 
                ft.Text(value='LEVEL 4', color="orange",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,size=30),
                ft.Text(value="Bárbaro",
                weight=ft.FontWeight.BOLD,
                size=30,
            color="black",
            ),
            ft.Text(value="O Bárbaro é um guerreiro destemido, com seu bigode imponente e seus músculos ele pode causar grandes estragos em aldeias inimigas. Solte uma horda destes bárbaros e espere para ver o caos!",
                    color="black",
                    text_align=ft.TextAlign.CENTER
            ),
            ]
        )
    )
        
    
    skills = ft.Container(
        expand=1,
        bgcolor="orange",
        padding=ft.padding.symmetric(horizontal=20),
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value="100",
                            color="white",
                            weight=ft.FontWeight.BOLD,
                            size=30
                        ),
                        ft.Text(
                            value="Dano",
                            color="white",
                        )
                        
                    ]
            
                ),
                ft.Column(
                    expand=1,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value="50",
                            color="white",
                            weight=ft.FontWeight.BOLD,
                            size=30
                        ),
                        ft.Text(
                            value="Velocidade",
                            color="white",
                        )
                    ]
                ),
                ft.Column(
                    expand=1,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value="40",
                            color="white",
                            weight=ft.FontWeight.BOLD,
                            size=30
                        ),
                        ft.Text(
                            value="Defesa",
                            color="white",
                        )
                    ]
                )
            ]
        )
    )

    layout = ft.Container(
        height=700,
        width=400,
        shadow=ft.BoxShadow(blur_radius=100, color="brown"),
        clip_behavior=ft.ClipBehavior.NONE,
        bgcolor="white",
        border_radius=ft.border_radius.all(30),
        content = ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills,
            ]
        )
    )
    page.add(layout)
    

if __name__ == '__main__':
    ft.app(target = main)
    
