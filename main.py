import flet as ft

async def main(page: ft.page):
    page.window_width = 720
    page.window_height = 1280
    page.window_resizable = False
    page.padding = 0
    
    superior = ft.Container(width=600, height=80, margin=ft.margin.only(top=40), border=ft.border.all())
    centro = ft.Container(width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all())
    inferior = ft.Container(width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all())
    
    
    col = ft.Column(spacing=0, controls=[
        superior,
        centro,
        inferior,
    ])
    
    contenedor = ft.Container(col, width=720, height=1280, bgcolor=ft.colors.RED, alignment=ft.alignment.top_center)
    
    await page.add_async(contenedor)

ft.app(target=main)