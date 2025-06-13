import flet as ft
import requests

API_URL = "http://localhost:8000/api/sociedades/"

def main(page: ft.Page):
    page.title = "Gestã de Sociedades da Igreja"

    def carregar_sociedade():
        response = requests.get(API_URL)
        if response.status_code == 200:
            sociedades = response.json()
            lista.controls.clear()
            for sociedade in sociedades:
                lista.controls.append(ft.Text(sociedade["nome"]))
            page.update()

    lista = ft.Column()
    botao_atualizar = ft.ElevatedButton("Carregar Sociedades",
                                        on_click=lambda e: carregar_sociedade())
    page.add(lista, botao_atualizar, lista)

ft.app(target=main)