from screens import MDApp, MDScreen, MDCard, MDLabel, MDBoxLayout, MDIconButton, MDWidget, data_animals_path, pd
from screens.components.left_navbar import add_left_navbar
from screens.components.open_navbar import open_nav_drawer

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.populate_cards()
        add_left_navbar(self)

    def read_animals_data(self):
        self.df_animals = pd.read_csv(data_animals_path, dtype={"peso":"float", "obs":"str"})
        #id,nome,tipo,peso,obs,cio,prenha,inseminado


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
        for index, animal in self.df_animals.iterrows():
            card = self.create_card(animal)

            for key, val in animal.items():
                if not key == "id":
                    card.add_widget(MDLabel(text=f"{key}: {val}", halign="left"))

            self.ids.animals_card_list.add_widget(card)


    def create_card(self, animal):
        card = MDCard(orientation="vertical",
                           size_hint=(0.9, None),
                          height="150dp",
                          pos_hint={"center_x": 0.5},
                          padding="20dp",
                          spacing="10dp")
        
        # Adiciona ícones para alterar e remover o cartão
        box_actions = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="10dp", spacing="8dp")
        edit_icon = MDIconButton(icon="pencil")
        edit_icon.bind(on_release=lambda x, animal=animal: self.edit_animal(animal))  # Chama a função de edição

        spacer = MDWidget(size_hint_x=.7)


        remove_icon = MDIconButton(icon="trash-can")
        remove_icon.bind(on_release=lambda x, animal=animal: self.remove_animal(animal))  # Chama a função de remoção

        box_actions.add_widget(edit_icon)
        box_actions.add_widget(spacer)
        box_actions.add_widget(remove_icon)

        card.add_widget(box_actions)

            
        return card

    def edit_animal(self, animal):
        self.manager.get_screen("Editcard").set_card(animal)     
        app = MDApp.get_running_app()
        app.change_screen("Editcard")  


    def remove_animal(self,animal):
        #animals_cards[:] = [ animal_card for animal_card in animals_cards if animal_card["id"]  != animal["id"]]
        self.df_animals = self.df_animals[self.df_animals["id"] != animal["id"]]
        self.df_animals.to_csv(data_animals_path, index= False)
        self.populate_cards()

    def open_nav_drawer(self):
        self.ids.nav_drawer.set_state("open")
