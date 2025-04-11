from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from uuid import uuid4
from kivymd.uix.widget import MDWidget
import pandas as pd
from os.path import join


users = [
    {"username": "admin", "password":"123"}
]

folder_data = "data"
data_animals_path = join("data","animals.csv")
df_animals = pd.read_csv(data_animals_path)
