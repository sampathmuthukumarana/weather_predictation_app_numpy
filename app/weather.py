import httpx

URL = "https://api.open-meteo.com/v1/forecast"

async def fetch_weather(lat: float, lon: float) -> dict:
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,"
                 "precipitation_sum,wind_speed_10m_max",
        "past_days": 7,
        "forecast_days": 1,
        "timezone": "auto",
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(URL, params=params)
        response.raise_for_status()
        return response.json()