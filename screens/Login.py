from screens import MDApp, MDScreen, users

class LoginScreen(MDScreen):
    def auth(self):
        username = self.ids.username.text
        password = self.ids.password.text
        app = MDApp.get_running_app()

        if username == "" or password == "":
            app.show_dialog("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        for user in users:
            if username == user["username"] and password == user["password"]:
                app.change_screen("Main")
                return 
        
        app.show_dialog("Usiuário não encontrado", "Login ou senha invalido")
