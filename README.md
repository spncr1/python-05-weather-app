# Weather App

## Description
Weather App is a simple desktop application built using Python and PyQt5 that allows users to quickly check the current weather in any city around the world. The application fetches live weather data from the OpenWeatherMap API and displays temperature, weather description, and a relevant emoji for visual appeal.  
This app is perfect for students, hobbyists, or anyone who wants a lightweight, no-frills weather checker right on their desktop.

## Features
- Search and display current weather for any city
- Shows temperature in Celsius
- Displays an emoji matching the weather condition (sunny, rainy, cloudy, etc.)
- Shows a text description of the current weather
- Clear, responsive error messages for invalid input or network issues
- Simple, modern PyQt5 GUI

## Getting Started

### Dependencies
- Python 3.10 or later (tested on Python 3.12)
- PyQt5
- requests

### Installation

1. **Clone or Download the Repo:**
   ```sh
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. **Install Required Packages:**
   ```sh
   pip install PyQt5 requests
   ```

3. **Run the Application:**
   ```sh
   python gui.py
   ```

### API Key Setup
This app uses a demo OpenWeatherMap API key. For production use, [get your free API key from OpenWeatherMap](https://openweathermap.org/appid) and replace the `api_key` value in `gui.py`.

## Usage

1. Launch the app:
   ```sh
   python gui.py
   ```
2. Enter a city name in the text field and click "Get Weather".
3. View the temperature, weather emoji, and weather description.

**Example:**

![Weather App Screenshot](./screenshot.png)

| Field          | Example Value             |
|----------------|--------------------------|
| City           | London                   |
| Temperature    | 18℃                      |
| Weather Emoji  | ☁                        |
| Description    | overcast clouds          |

## Folder Structure

```
weather-app/
├── gui.py           # Main application file
├── README.md        # Project documentation
└── screenshot.png   # GUI screenshot (add your own for reference)
```

## Contributing

Contributions are welcome!  
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with clear description of changes.

Feel free to suggest features, report bugs, or submit fixes.

## License

MIT License  
See [LICENSE](./LICENSE) for details.

## Author

Spencer [spncr1]  
GitHub: [github.com/spncr1](https://github.com/spncr1)