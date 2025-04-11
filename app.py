from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from screens.Login import LoginScreen
from screens.Signup import SignUpScreen
from screens.Main import MainScreen
from screens.Newcard import NewCardScreen
from screens.EditCard import EditCardScreen
from screens.Metrics import MetricsScreen
from screens.Dashboard import DashboardScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp
from os.path import join

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Define o tema como Light77
        self.theme_cls.primary_palette = "Blue"  # Adiciona uma paleta de cores primária
        
        Builder.load_file(join("kv_files", "login_screen.kv"))
        Builder.load_file(join("kv_files", "signup_screen.kv"))
        Builder.load_file(join("kv_files", "main_screen.kv"))
        Builder.load_file(join("kv_files", "newcard_screen.kv"))
        Builder.load_file(join("kv_files", "editcard_screen.kv"))
        Builder.load_file(join("kv_files", "metrics_screen.kv"))
        Builder.load_file(join("kv_files", "dashboard_screen.kv"))

        self.sm = MDScreenManager()

        self.sm.add_widget(LoginScreen(name="Login"))
        self.sm.add_widget(SignUpScreen(name="Signup"))
        self.sm.add_widget(MainScreen(name="Main"))
        self.sm.add_widget(MetricsScreen(name="Metrics"))
        self.sm.add_widget(NewCardScreen(name="Newcard"))
        self.sm.add_widget(EditCardScreen(name="Editcard"))
        self.sm.add_widget(DashboardScreen(name="Dashboard"))
        
        return self.sm


    def show_dialog(self, title, message):
        self.dialog = MDDialog(title=title, 
                                   text=message,
                                    buttons = [MDFlatButton(text="Fechar", on_release= lambda _: self.dialog.dismiss())] )
        self.dialog.open()

    def change_screen(self, screen):
        
        self.sm.current = screen
        
        if "update_animals_data" in  dir(self.sm.get_screen(screen )):
            self.sm.get_screen(screen ).update_animals_data()

        ids = self.sm.get_screen(screen).ids
        if "nav_drawer" in ids:
            ids.nav_drawer.set_state("close")

    
if __name__ == "__main__":
    MyApp().run()