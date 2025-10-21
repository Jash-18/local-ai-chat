# ChatGPT-Like Mobile App with Kivy
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
import requests
import json
import threading
from datetime import datetime

class ChatMessage(BoxLayout):
    def __init__(self, message, is_user=True, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = '48dp'
        self.spacing = '10dp'
        self.padding = ['10dp', '5dp']
        
        # Create background color
        with self.canvas.before:
            Color(0.2, 0.6, 1.0, 1.0) if is_user else Color(0.9, 0.9, 0.9, 1.0)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self.update_rect, pos=self.update_rect)
        
        # Message label
        label = Label(
            text=message,
            text_size=(None, None),
            halign='left',
            valign='middle',
            color=[1, 1, 1, 1] if is_user else [0, 0, 0, 1]
        )
        
        self.add_widget(label)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class ChatInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = '10dp'
        self.padding = ['10dp']
        
        # API Configuration - Updated with your IP address
        self.api_url = "http://10.95.151.162:1234/v1/chat/completions"  # Your laptop IP
        self.model_name = "local-model"
        
        # Title
        title = Label(
            text='Local AI Assistant',
            size_hint_y=None,
            height='50dp',
            font_size='20sp',
            bold=True
        )
        self.add_widget(title)
        
        # Chat history container
        self.chat_scroll = ScrollView()
        self.chat_container = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing='5dp'
        )
        self.chat_container.bind(minimum_height=self.chat_container.setter('height'))
        self.chat_scroll.add_widget(self.chat_container)
        self.add_widget(self.chat_scroll)
        
        # Input area
        input_layout = BoxLayout(
            size_hint_y=None,
            height='50dp',
            spacing='10dp'
        )
        
        self.message_input = TextInput(
            multiline=False,
            hint_text='Type your message here...',
            size_hint_x=0.8
        )
        self.message_input.bind(on_text_validate=self.send_message)
        
        self.send_button = Button(
            text='Send',
            size_hint_x=0.2
        )
        self.send_button.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.message_input)
        input_layout.add_widget(self.send_button)
        self.add_widget(input_layout)
        
        # Status label
        self.status_label = Label(
            text='Connected to: 10.95.151.162:1234',
            size_hint_y=None,
            height='30dp',
            font_size='12sp'
        )
        self.add_widget(self.status_label)
        
        # Add welcome message
        self.add_chat_message("Hello! I'm your local AI assistant running on your laptop (10.95.151.162). How can I help you today?", False)
    
    def add_chat_message(self, message, is_user=True):
        chat_msg = ChatMessage(message, is_user)
        self.chat_container.add_widget(chat_msg)
        
        # Auto-scroll to bottom
        Clock.schedule_once(lambda dt: setattr(self.chat_scroll, 'scroll_y', 0), 0.1)
    
    def send_message(self, *args):
        user_message = self.message_input.text.strip()
        if not user_message:
            return
        
        # Add user message to chat
        self.add_chat_message(user_message, True)
        
        # Clear input
        self.message_input.text = ""
        
        # Update status
        self.status_label.text = "Thinking..."
        
        # Send to AI in separate thread
        threading.Thread(target=self.get_ai_response, args=(user_message,), daemon=True).start()
    
    def get_ai_response(self, message):
        try:
            headers = {
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model_name,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant running locally on the user's laptop. Be concise and friendly."
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                "max_tokens": 150,
                "temperature": 0.7
            }
            
            response = requests.post(self.api_url, json=payload, headers=headers, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                ai_message = data['choices'][0]['message']['content']
                Clock.schedule_once(lambda dt: self.add_ai_response(ai_message), 0)
            else:
                error_msg = f"Error: Server returned {response.status_code}"
                Clock.schedule_once(lambda dt: self.add_ai_response(error_msg), 0)
                
        except requests.exceptions.ConnectionError:
            error_msg = "Connection failed. Make sure LM Studio server is running on 10.95.151.162:1234"
            Clock.schedule_once(lambda dt: self.add_ai_response(error_msg), 0)
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            Clock.schedule_once(lambda dt: self.add_ai_response(error_msg), 0)
        
        # Update status
        Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', 'Connected to: 10.95.151.162:1234'), 0)
    
    def add_ai_response(self, message):
        self.add_chat_message(message, False)

class LocalAIApp(App):
    def build(self):
        return ChatInterface()

if __name__ == '__main__':
    LocalAIApp().run()