import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Metric for °C
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        return f"""
        Weather in {city_name}:
        🌡 Temperature: {temp}°C
        🌤 Condition: {weather}
        💧 Humidity: {humidity}%
        🌬 Wind Speed: {wind_speed} m/s
        """
    else:
        return f"Error: {data.get('message', 'Unable to fetch weather data')}"

if __name__ == "__main__":
    # Get your free API key from https://openweathermap.org/api
    API_KEY = "7d6a51925744caf93d3a39d8bccbbd98"  
    
    city = input("Enter city name: ")
    print(get_weather(city, API_KEY))   
