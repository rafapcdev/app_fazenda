from screens import MDScreen, MDApp, data_animals_path, pd


class EditCardScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_card(self, animal):
        self.animal_id = animal["id"]

        self.ids.animal_name.text = animal["nome"]
        self.ids.animal_type.text = animal["tipo"]
        self.ids.animal_weight.text = str(animal["peso"])
        self.ids.animal_obs.text =  animal["obs"] if not pd.isna(animal["obs"]) else ""
        self.ids.checkbox_on_heat.active = animal["cio"]
        self.ids.checkbox_is_pregnant.active = animal["prenha"]
        self.ids.checkbox_inseminated.active = animal["inseminado"]
         
    def update_card(self):
        app = MDApp.get_running_app()
        
        animal_nome = self.ids.animal_name.text
        animal_tipo = self.ids.animal_type.text
        animal_peso = self.ids.animal_weight.text
        animal_obs = self.ids.animal_obs.text
        animal_cio = self.ids.checkbox_on_heat.active,
        animal_prenha = self.ids.checkbox_is_pregnant.active,
        animal_inseminado = self.ids.checkbox_inseminated.active

        
        animal = {
            "id": self.animal_id,
            "nome": animal_nome,
            "tipo": animal_tipo,
            "peso": animal_peso,
            "obs": animal_obs,
            "cio": animal_cio,
            "prenha": animal_prenha,
            "inseminado": animal_inseminado
        }

        if not animal_nome or not animal_tipo or not animal_peso:
            app.show_dialog("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return
        
        df_animal = pd.read_csv(data_animals_path)

        mask = df_animal["id"] == animal["id"]
        for col, value in animal.items():
            if col == "peso":
                value = float(value)
            df_animal.loc[mask, col] = value

        df_animal.to_csv(data_animals_path, index=False)
        

        #self.manager.get_screen("Main").update_animals_data()
        app.change_screen("Main")


