import requests
import os

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8 * forecast_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Wloclawek", forecast_days=2))
