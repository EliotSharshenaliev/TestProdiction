import json
import threading

import requests
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

KV = """
<MDScreenManager>:
    MainScreen:
    
<MainScreen>:
    name: "main_screen"
    MDBoxLayout:
        md_bg_color: "white"
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        MDLabel:
            pos_hint: {"center_x": .5, "center_y": .5}
            text: root.ip_address
            halign: "center"
            bold: True
"""


class MainScreen(MDScreen):
    ip_address = StringProperty(defaultvalue="Getting...")

    def on_enter(self):
        threading.Thread(target=self.set_ip, args=[]).start()

    def set_ip(self):
        r = requests.get('https://api.ipify.org?format=json')
        response: dict = json.loads(r.content)
        self.ip_address = f"Ip Address: {response.get('ip')}"


class GetIpApp(MDApp):
    def build(self):
        Builder.load_string(KV)
        sc = MDScreenManager()
        sc.current = "main_screen"
        return sc


if __name__ == "__main__":
    GetIpApp().run()
