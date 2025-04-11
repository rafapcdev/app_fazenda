from kivymd.uix.boxlayout import MDBoxLayout
from screens.components.matplotlib_backend import MatplotlibImage
import seaborn as sns
from screens import MDScreen, data_animals_path, pd
import matplotlib.pyplot as plt
from screens.components.left_navbar import add_left_navbar
import pandas as pd

class DashboardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.read_animals_data()
        add_left_navbar(self)
        self.create_graphs()

    def read_animals_data(self):
        self.df_animals = pd.read_csv(data_animals_path, dtype={"peso":"float", "obs":"str"})
        #id,nome,tipo,peso,obs,cio,prenha,inseminado

    def update_animals_data(self):
        self.read_animals_data()
        self.ids.graph_container.clear_widgets()
        self.create_graphs()
    
    def create_graphs(self):
        # Obtenha o graph_container usando o id definido no KV
        graph_container = self.ids.graph_container
        
        # Crie um novo layout para os gráficos
        layout = MDBoxLayout(orientation='vertical', padding='10dp', spacing='10dp')


        # data
        df_melt = self.df_animals.melt(id_vars=("id"), value_vars=("cio", "prenha", "inseminado"), var_name="tipo",value_name="valor")
        df_plot_by_type = df_melt.groupby("tipo").agg(n=("valor","sum")).reset_index() 

        # Gráfico 1 - Matplotlib básico
        fig1 = plt.Figure(figsize=(5, 3), dpi=100)
        ax1 = fig1.add_subplot(111)

        sns.barplot(data=df_plot_by_type, x="tipo",y="n", hue="tipo", errorbar=None, ax=ax1)
        ax1.set_ylabel("Quantidade")
        ax1.set_title("Avaliação status ")

        # Gráfico 2 - Matplotlib básico
        fig2 = plt.Figure(figsize=(5, 3), dpi=100)
        ax2 = fig2.add_subplot(111)
        sns.histplot(data=self.df_animals, x="peso", ax=ax2)
        ax2.set_xlabel("Peso em kg")
        ax2.set_title("Histograma de pesos ")


        # Adiciona o gráfico ao layout
        layout.add_widget(MatplotlibImage(figure=fig1, size_hint_y=0.5))
        layout.add_widget(MatplotlibImage(figure=fig2, size_hint_y=0.5))
        
        # Adicione o layout com o gráfico ao graph_container
        graph_container.add_widget(layout)

    def open_nav_drawer(self):
        nav_drawer = self.ids.nav_drawer
        nav_drawer.set_state("open")