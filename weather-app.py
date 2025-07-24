# WEATHER APP
# API KEY used: 6c006d30b85f330a0202c99bfd528b19
# using PyQt5, which is a library that allows you to use the Qt framework from Python
# using print(data) we can find the individual variable that relates to what we want i.e., weather description, weather value etc. and that's where we see something like 'description' be used
# we use that to extrapolate the unique identifier for what we want to display, store it within a variable, and then use the properties of our Qt class to display it within our app

import sys
import requests
from PyQt5.QtWidgets import * # but we're only using: (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout)

from PyQt5.QtCore import Qt
from requests import RequestException
from socks import HTTPError

# class definition, defining our core elements
class WeatherApp(QWidget):
    def __init__(self): # self = weather app object
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self) # label that prompts a user to enter in a city
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self) # makes a request to an API when clicked
        self.temperature_label = QLabel(self) # placeholder (remove this later)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    # initialise UI
    def initUI (self):
        self.setWindowTitle("Weather App") # keep as 'Weather App' for now, but can change the name later

        # layout manager of our widgets
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.city_input, alignment=Qt.AlignCenter)
        vbox.addWidget(self.get_weather_button, alignment=Qt.AlignCenter)
        vbox.addWidget(self.temperature_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.emoji_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.description_label, alignment=Qt.AlignCenter)
        self.setLayout(vbox)

        # Applying styles based on object names
        self.city_label.setObjectName('city_label') # 'city_label' = unique ID for the widget
        self.city_input.setObjectName('city_input')
        self.get_weather_button.setObjectName('get_weather_button')
        self.temperature_label.setObjectName('temperature_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')

        # Style Sheet (styling properties)
        # QLabel = the class, where we can list multiple CSS properties
        # different labels require different classes to customize their style in the window
        # this needs to be fixed: the text field is currently TOO SMALL, need to be able to customise and alter it seamlessly
        # QLineEdit#city_input{
        #                     font-size: 30px;
        #                 }
        self.setStyleSheet(""" 
            QLabel {
                font-family: calibri;
                }
                QLabel#city_label{
                    font-size: 40px;
                    font-style: italic;
                }
                QLineEdit#city_input{
                    font-size: 40px;
                }
                QPushButton#get_weather_button{
                    font-size: 30px;
                    font-weight: bold;
                }
                QLabel#temperature_label{
                    font-size: 70px;
                }
                QLabel#emoji_label{
                    font-size: 100px;
                    font-family: Segoe UI emoji;
                }
                QLabel#description_label{
                    font-size: 50px;
                }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        #local to get_weather function
        api_key = "6c006d30b85f330a0202c99bfd528b19"
        city = self.city_input.text() # used to get the text entered from the line edit widget using text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" # f-String link for a built-in API request to get current weather data from our weather website: https://openweathermap.org/

        # enclose any code that may cause an exception within a try-catch block
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json() # convert our response object into JSON format

            if data["cod"] == 200: # i.e., if the error code = 200, the API request was successful
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error: # error codes of 400-499 indicate client error responses, where error codes of 500-599 indicate server error responses
            match response.status_code:
                case 400: # bad request
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorised:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is Denied")
                case 404:
                    self.display_error("Not Found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _: # if we have no matching cases for the above, then the below gets executed as a wildcard case
                    self.display_error(f"HTTP error occurred\n{http_error}")

        except requests.exceptions.ConnectionError :
            self.display_error("Connection Error\nPlease check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as request_error:
            self.display_error(f"Request Error:\n{request_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;") #NOTE: this text is not centre aligned FFS
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 70px;")
        temperature_k = data['main']['temp']
        temperature_c = temperature_k - 273.15 # converting temperature in Kelvin to degrees Celsius
        # note: the weather id is essentially a 3-digit code that represents the description of the weather i.e., clear skies, or cloudy
        weather_id = data['weather'][0]['id'] # weather is a list of a dictionary, and all we're doing is accessing the key of "id" at index 0
        weather_description = data['weather'][0]['description']

        self.temperature_label.setText(f"{temperature_c:.0f}℃") # format specified to round up to the nearest degree
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(f"{weather_description}")

    # this function doesn't rely on any class/instance data
    @staticmethod #belongs to a class, but doesn't require any instance-specific data or any other methods
    def get_weather_emoji(weather_id):
        # either a match-case or else-if statements would work here i.e., if the weather id falls within a specific range, a specific emoji is printed that corresponds to this information
        # this information can all be found on the website we're using
        if 200 <= weather_id <= 232:
            return "🌩️"
        elif 300 <= weather_id <= 321:
            return "💧"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "⛄"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return  "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return  "☁"
        else: # if there are no matches, we don't show anything
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp() # calling weather app object
    weather_app.show()
    sys.exit(app.exec_())