from screens import MDScreen, MDApp, uuid4, pd, data_animals_path

class NewCardScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_card(self):
        app = MDApp.get_running_app()
        
        animal_nome = self.ids.animal_name.text
        animal_tipo = self.ids.animal_type.text
        animal_peso = self.ids.animal_weight.text
        animal_obs =  self.ids.animal_obs.text
        animal_cio = self.ids.checkbox_on_heat.active,
        animal_prenha = self.ids.checkbox_is_pregnant.active,
        animal_inseminado = self.ids.checkbox_inseminated.active

        if not animal_nome or not animal_tipo or not animal_peso:
            app.show_dialog("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        animal = {
            "id": uuid4().hex,
            "nome": animal_nome,
            "tipo": animal_tipo,
            "peso": float(animal_peso),
            "obs": animal_obs,
            "cio": animal_cio,
            "prenha": animal_prenha,
            "inseminado": animal_inseminado
        }
        
        # animals_cards.append(animal)
        new_animal = pd.DataFrame(animal)
        df_animals = pd.read_csv(data_animals_path)
        df_animals = pd.concat([df_animals, new_animal], axis=0)
        df_animals.to_csv(data_animals_path, index=False)

        self.clear_form()
        app.change_screen("Main")

    def clear_form(self):
        self.ids.animal_name.text = ""
        self.ids.animal_type.text = ""
        self.ids.animal_weight.text = ""
        self.ids.animal_obs.text= ""
        self.ids.checkbox_on_heat.active= ""
        self.ids.checkbox_is_pregnant.active = ""
        self.ids.checkbox_inseminated.active = ""
    
    def fiil_form(self):
        self.ids.animal_name.text = "vaca"
        self.ids.animal_type.text = "Bovino"
        self.ids.animal_weight.text = "123"
        self.ids.animal_obs.text= ""
        self.ids.checkbox_on_heat.active= True
        self.ids.checkbox_is_pregnant.active = True
        self.ids.checkbox_inseminated.active = True