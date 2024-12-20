from dataclasses import dataclass

@dataclass
class CityInfo:
    name: str
    country: str
    region: str
    importance: float
    maps_url: str
