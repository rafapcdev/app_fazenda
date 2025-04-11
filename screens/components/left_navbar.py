from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

left_navbar = [
    {"label": "Animais", "screen": "Main"},
    {"label": "Metricas", "screen": "Metrics"},
    {"label": "Gráficos", "screen": "Dashboard"},
    
]

def add_left_navbar(self):
    nav = self.ids.left_navbar
    app = MDApp.get_running_app()
    
    # Limpa os itens existentes
    nav.clear_widgets()
    
    for page in left_navbar:
        # Cria o item com a função lambda corretamente
        item = OneLineListItem(
            text=page["label"],
            on_release=lambda x, screen=page["screen"]: app.change_screen(screen)
        )
        nav.add_widget(item)
    
    # Força a atualização do layout (opcional, mas pode ajudar)
    nav.do_layout()