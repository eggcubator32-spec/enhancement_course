# Weather Dashboard

A modern Python weather dashboard application that fetches real-time weather data from the OpenWeatherMap API with a command-line interface and optional web dashboard.

## Overview

This project provides a comprehensive weather dashboard that:

- **Real-time Weather Data**: Fetch current weather conditions for any location
- **Forecast Data**: Get 5-day weather forecasts
- **Multi-location Support**: Check weather for multiple cities
- **Caching**: Cache API responses to minimize requests and improve performance
- **Error Handling**: Robust error handling and logging
- **Command-line Interface**: Easy-to-use CLI for weather queries
- **Data Visualization**: Display weather data in a clean, readable format

## Features

✅ **Current Weather** - Temperature, humidity, wind speed, pressure, visibility  
✅ **Weather Forecasts** - 5-day forecasts with hourly data  
✅ **Multiple Locations** - Support for cities worldwide  
✅ **Caching System** - Reduce API calls with intelligent caching  
✅ **Error Handling** - Graceful error handling and logging  
✅ **Type Safety** - Full type hints throughout  
✅ **Unit Conversion** - Support for Celsius, Fahrenheit, Kelvin  
✅ **Weather Alerts** - Alert display for severe weather conditions  

## Project Structure

```
weather_dashboard/
├── main.py              # Main application and CLI
├── weather_api.py       # OpenWeatherMap API client
├── models.py            # Weather data models
├── cache.py             # Response caching system
├── formatter.py         # Data formatting and display
├── config.py            # Configuration and constants
├── requirements.txt     # Project dependencies
└── README.md            # This file
```

## Installation

1. Clone or download this project:
   ```bash
   cd weather_dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api):
   - Sign up for a free account
   - Navigate to API keys section
   - Copy your API key

4. Set your API key as an environment variable:
   ```bash
   export OPENWEATHER_API_KEY="your_api_key_here"
   ```

   Or create a `.env` file:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Usage

### Command Line Interface

#### Get Current Weather
```bash
python main.py --city "London"
python main.py --city "New York" --units fahrenheit
python main.py --city "Tokyo" --units metric
```

#### Get Weather Forecast
```bash
python main.py --city "Paris" --forecast
python main.py --city "Sydney" --forecast --days 3
```

#### Search Multiple Cities
```bash
python main.py --cities "London,Paris,Tokyo"
python main.py --cities "New York,Los Angeles,Chicago" --forecast
```

#### Clear Cache
```bash
python main.py --clear-cache
```

#### Show Help
```bash
python main.py --help
```

### Using in Your Code

```python
from weather_api import WeatherAPI
from config import OPENWEATHER_API_KEY

# Initialize API client
weather = WeatherAPI(api_key=OPENWEATHER_API_KEY)

# Get current weather
current = weather.get_current_weather("London")
print(f"Temperature: {current.temperature}°C")
print(f"Condition: {current.condition}")
print(f"Humidity: {current.humidity}%")

# Get forecast
forecast = weather.get_forecast("London")
for day in forecast:
    print(f"{day.date}: {day.condition}, {day.temp_max}°C")

# Get weather for multiple cities
cities = ["London", "Paris", "Tokyo"]
for city in cities:
    weather_data = weather.get_current_weather(city)
    print(f"{city}: {weather_data.temperature}°C, {weather_data.condition}")
```

## API Reference

### WeatherAPI Class

#### Methods

- `get_current_weather(city: str, units: str = 'metric') -> CurrentWeather` - Fetch current weather
- `get_forecast(city: str, units: str = 'metric') -> List[Forecast]` - Fetch 5-day forecast
- `get_weather_by_coordinates(lat: float, lon: float, units: str = 'metric') -> CurrentWeather` - Get weather by lat/lon
- `search_city(city_name: str) -> List[CityInfo]` - Search for city information

### Data Models

#### CurrentWeather
```python
@dataclass
class CurrentWeather:
    city: str
    country: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    visibility: int
    wind_speed: float
    wind_deg: int
    clouds: int
    condition: str
    description: str
    icon: str
    sunrise: datetime
    sunset: datetime
    timezone: int
```

#### Forecast
```python
@dataclass
class Forecast:
    date: str
    time: str
    temperature: float
    temp_min: float
    temp_max: float
    humidity: int
    pressure: int
    wind_speed: float
    condition: str
    description: str
    precipitation: float
```

## Configuration

Edit `config.py` to customize:

```python
# API settings
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5'

# Cache settings
CACHE_EXPIRATION_HOURS = 1
CACHE_DIR = 'weather_cache'

# Default units
DEFAULT_UNITS = 'metric'  # metric, imperial, standard

# Display settings
DISPLAY_FORMAT = 'detailed'  # detailed, compact, json
```

## Output Examples

### Current Weather (Detailed)
```
┌─────────────────────────────────────┐
│ Weather for London, GB              │
├─────────────────────────────────────┤
│ Temperature:       15°C (feels: 14°C)│
│ High/Low:         18°C / 12°C        │
│ Condition:        Partly Cloudy      │
│ Humidity:         65%                │
│ Wind:             12 km/h (NW)       │
│ Pressure:         1013 mb            │
│ Visibility:       10 km              │
│ Sunrise:          06:45 AM           │
│ Sunset:           08:30 PM           │
└─────────────────────────────────────┘
```

### Forecast
```
London 5-Day Forecast
═══════════════════════════════════════
Day 1 (Mon) - Partly Cloudy
  High: 18°C | Low: 12°C | Humidity: 65%
Day 2 (Tue) - Rainy
  High: 16°C | Low: 10°C | Humidity: 80%
Day 3 (Wed) - Cloudy
  High: 17°C | Low: 11°C | Humidity: 70%
...
```

## Environment Variables

```bash
OPENWEATHER_API_KEY          # Your OpenWeatherMap API key
WEATHER_CACHE_EXPIRATION     # Cache expiration in hours (default: 1)
WEATHER_DEFAULT_UNITS        # Default temperature units (metric/imperial/standard)
```

## Error Handling

The application gracefully handles:

- Invalid API keys
- Network connectivity issues
- Invalid city names
- Rate limiting
- API service unavailability
- Cache errors

All errors are logged with helpful messages.

## Caching

The application implements intelligent caching:

- Responses are cached for 1 hour by default
- Cache directory: `weather_cache/`
- Automatic cache cleanup
- Manual cache clearing with `--clear-cache` flag

## Requirements

- Python 3.7+
- requests library
- python-dotenv library

## Performance

- API calls are cached to minimize requests
- Batch requests for multiple cities
- Efficient JSON parsing
- Optimized display rendering

## Troubleshooting

### "API key is invalid"
- Verify your API key is correct
- Check it's set in environment variables or .env file
- Ensure your OpenWeatherMap account is active

### "City not found"
- Try using the full city name with country code: "London, GB"
- Check spelling and capitalization

### "Too many requests"
- You may have exceeded the API rate limit
- Check your account plan on OpenWeatherMap
- The cache helps reduce requests

### Network errors
- Check your internet connection
- Verify the API endpoint is accessible
- Check firewall/proxy settings

## API Limits

**Free Plan:**
- 60 calls/minute
- 1,000,000 calls/month
- Current weather + forecast data

**Paid Plans:**
- Higher rate limits
- Additional features available

## Resources

- [OpenWeatherMap Documentation](https://openweathermap.org/api)
- [OpenWeatherMap FAQ](https://openweathermap.org/faq)
- [Weather Conditions](https://openweathermap.org/weather-conditions)
- [Python Requests Library](https://docs.python-requests.org/)

## License

This project is provided as an educational example.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify your API key and configuration
3. Review the OpenWeatherMap documentation
4. Check application logs for error details
