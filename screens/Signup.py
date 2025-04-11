from screens import MDApp, MDScreen, users

class SignUpScreen(MDScreen):
    def sign(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        app = MDApp.get_running_app()
            

        if not username or not password:
            app.show_dialog("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        # Verifica se usuário já existe
        for user in users:
            if username == user["username"]:
                app.show_dialog("Erro", "Usuário já existe")
                return

        # Adiciona novo usuário
        users.append({"username": username, "password": password})
        app.change_screen("Main")

