import random
import requests

from core.models import CityInfo

class CityAPI:
    def fetch_city_info(self, city_name: str) -> CityInfo | None:
        url = f"https://nominatim.openstreetmap.org/search?city={city_name}&format=json&accept-language=ru"
        headers = {"User-Agent": "CityInfoBot/1.0 (contact@example.com)"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None
        data = response.json()
        if data:
            city = data[0]
            display_name = city.get("display_name", "Неизвестно").split(", ")

            return CityInfo(
                name=display_name[0],
                country=display_name[-1],
                region=display_name[1],
                importance=city.get("importance", {"Неизвестно"}),
                maps_url=f"https://www.google.com/maps/search/?api=1&query={city['lat']},{city['lon']}"
            )
        return None

    def fetch_random_city(self) -> CityInfo | None:
        cities = ["Москва", "Париж", "Токио", "Нью-Йорк", "Лондон", "Рио-де-Жанейро", "Сидней", "Шанхай", "Дубай", "Каир"]
        city_name = random.choice(cities)
        return self.fetch_city_info(city_name)