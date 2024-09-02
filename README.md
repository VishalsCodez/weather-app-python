# Weather App by Vishal Sagi

## Overview

This is a simple weather app built using Flask. It allows users to enter a city name to get the current weather and also offers a 5-day forecast. The app can also fetch weather information based on the user's current location.

## Features

- Enter a city to get the current weather.
- View a 5-day weather forecast.
- Fetch weather information based on the user's location.
- Display weather icons based on current conditions.
- Includes an info button with details about the PM Accelerator.

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/weather-app-python.git
    ```

2. Navigate to the project directory:

    ```bash
    cd weather-app-python
    ```

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up the environment variables:

    Create a `.env` file in the root directory and add your OpenWeatherMap API key:

    ```plaintext
    OPENWEATHER_API_KEY=your_openweathermap_api_key
    ```

6. Run the application:

    ```bash
    flask run
    ```

7. Open a web browser and go to `http://127.0.0.1:5000`.

## Technologies Used

- Python
- Flask
- HTML/CSS
- JavaScript
- OpenWeatherMap API

## Author

Vishal Sagi

## About PM Accelerator

PM Accelerator is a program designed to help aspiring product managers develop their skills through real-world projects and mentorship. It provides participants with the opportunity to work on innovative products and collaborate with industry professionals. For more information, visit the PM Accelerator [LinkedIn page](https://www.linkedin.com/company/pm-accelerator/).
