from screens import MDApp, MDScreen, MDCard, MDLabel, MDBoxLayout, data_animals_path
from screens.components.left_navbar import add_left_navbar
import pandas as pd


class MetricsScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.populate_cards()
        add_left_navbar(self)
    
    def read_animals_data(self):
        self.df_animals = pd.read_csv(data_animals_path)

    def update_animals_data(self):
        self.read_animals_data()
        self.populate_cards()


    def populate_cards(self):       
        self.read_animals_data()

        if self.df_animals.shape[0] == 0:
            self.ids.animals_card_list.clear_widgets()

            card = MDCard(orientation="vertical",
                           size_hint=(0.9, None),
                          height="150dp",
                          pos_hint={"center_x": 0.5},
                          padding="10dp",
                          spacing="10dp")
            
            card.add_widget(MDLabel(text="Nenhum card existente", halign="center"))
            self.ids.animals_card_list.add_widget(card)
            return
        
        self.ids.animals_card_list.clear_widgets()
        
        cows_inseminated = self.df_animals[self.df_animals["inseminado"] == True].shape[0]
        self.create_card("Inseminação", {
            "Quantidade de vacas inseminadas": str(cows_inseminated),
            "Taxa de serviço": f"RS  {str(cows_inseminated * 100)}" })
        

        cows_on_heat = self.df_animals[self.df_animals["prenha"] == True].shape[0]
        self.create_card("Cio", {
            "Quantidade de vacas em cio": str(cows_on_heat),
            "Taxa de serviço": f"RS  {str(cows_on_heat * 100)}" })
        
        cows_pregnant = self.df_animals[self.df_animals["cio"] == True].shape[0]
        self.create_card("Prenhas", {
            "Quantidade de vacas prenhas": str(cows_pregnant),
            "Taxa de serviço": f"RS  {str(cows_pregnant * 100)}" })



    def create_card(self, title, obj):

        card = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="150dp",
            pos_hint={"center_x": 0.5},
            padding="20dp",
            spacing="10dp"
        )

        # Criação do layout para o card
        card_layout = MDBoxLayout(orientation="vertical", spacing="10dp")

        # Adicionando o título ao card
        card_title = MDLabel(
            text= title,
            size_hint_y=None,
            height="30dp",  # Defina uma altura fixa para o título
            halign="center",  # Centraliza o texto
            theme_text_color="Primary"  # Define a cor do texto do tema
        )

        # Adicionando o título ao layout do card
        card_layout.add_widget(card_title)

        for key, val  in obj.items():
        # Adicionando as informações ao card
            item = MDLabel(text=f"{key}: {val}")
            card_layout.add_widget(item)



        # Adicionando o layout ao card
        card.add_widget(card_layout)

        # Adicionando o card à lista de cards
        self.ids.animals_card_list.add_widget(card)

    # def cows_on_heat(self):
    #     count = 0
    #     for animal_card in animals_cards:
    #         if animal_card["name"].lower() == "vaca":
    #             count += 1 if "Cio" in animal_card["status"] else 0

        
    #     return count

    # def cows_pregnant(self):
    #     count = 0
    #     for animal_card in animals_cards:
    #         if animal_card["name"].lower() == "vaca":
    #             count += 1 if "Prenha" in animal_card["status"] else 0

        
    #     return count
    
    def open_nav_drawer(self):
        self.ids.nav_drawer.set_state("open")