from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import pytz
import requests

app = Flask(__name__)

def get_Weather(searchCity):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{searchCity}?unitGroup=us&key=6E8UAWY68C8GLU7MKYSWSG3PL&contentType=json"
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = response.json()
        location = data['address']
        timezone = data["timezone"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        days = data['days']
        today = days[0]
        tomorrow = days[1] if len(days) > 1 else {"hours": []}

        # Use city's local timezone
        local_tz = pytz.timezone(timezone)
        now = datetime.now(local_tz)
        current_hour = now.hour

        icon_mapping = {
            "clear-day": "wi-day-sunny",
            "clear-night": "wi-night-clear",
            "partly-cloudy-day": "wi-day-cloudy",
            "partly-cloudy-night": "wi-night-alt-cloudy",
            "cloudy": "wi-cloudy",
            "rain": "wi-rain",
            "showers-day": "wi-day-showers",
            "showers-night": "wi-night-alt-showers",
            "snow": "wi-snow",
            "snow-showers-day": "wi-day-snow",
            "snow-showers-night": "wi-night-alt-snow",
            "wind": "wi-windy",
            "fog": "wi-fog",
            "thunderstorm": "wi-thunderstorm"
        }

        hourly_forecast = []

        for hour in today['hours'][current_hour:]:
            hour_dt = int(hour['datetime'].split(':')[0])
            is_now = hour_dt == current_hour
            hourly_forecast.append({
                "time": "Now" if is_now else f"{hour_dt:02d}:00",
                "temp": round((hour['temp'] - 32) * 5/9, 2),
                "windspeed": hour['windspeed'],
                "icon_class": icon_mapping.get(hour.get("icon", ""), "wi-na"),
                "is_now": is_now
            })

        remaining_hours = 24 - len(hourly_forecast)
        for hour in tomorrow['hours'][:remaining_hours]:
            hour_dt = int(hour['datetime'].split(':')[0])
            hourly_forecast.append({
                "time": f"{hour_dt:02d}:00",
                "temp": round((hour['temp'] - 32) * 5/9, 2),
                "windspeed": hour['windspeed'],
                "icon_class": icon_mapping.get(hour.get("icon", ""), "wi-na"),
                "is_now": False
            })

        matched_hour = next((h for h in hourly_forecast if h["is_now"]), None)

        return {
            "city": location,
            "timezone": timezone,
            "latitude": latitude,
            "longitude": longitude,
            "temp": round((today['temp'] - 32) * 5/9, 2),
            "tempmin": round((today['tempmin'] - 32) * 5/9, 2),
            "tempmax": round((today['tempmax'] - 32) * 5/9, 2),
            "feelslike": round((today['feelslike'] - 32) * 5/9, 2),
            "humidity": today['humidity'],
            "windspeed": today['windspeed'],
            "winddir": today['winddir'],
            "pressure": today["pressure"],
            "sunriseTime": today['sunrise'],
            "sunsetTime": today['sunset'],
            "icon": matched_hour["icon_class"] if matched_hour else "wi-na",
            "icon_class": matched_hour["icon_class"] if matched_hour else "wi-na",
            "hourly": hourly_forecast,
            "local_time": now.strftime("%I:%M %p"),
            "local_date": now.strftime("%A, %d %B")
        }

    errorCode = response.status_code
    errorMessage = response.text
    return redirect(url_for('error', errorCode=errorCode, errorMessage=errorMessage))


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("searchCity")
        return redirect(url_for('city_day', city=city))
    result = get_Weather("Patna")
    return render_template('index.html', weather=result)


@app.route('/cityDay')
def city_day():
    city = request.args.get("city", default="Patna")
    result = get_Weather(city)

    if not isinstance(result, dict):
        return result

    # Get timezone-aware "now" time
    city_timezone = pytz.timezone(result["timezone"])
    now = datetime.now(city_timezone)

    # Parse sunrise and sunset as timezone-aware
    sunrise = city_timezone.localize(datetime.strptime(result['sunriseTime'], "%H:%M:%S"))
    sunset = city_timezone.localize(datetime.strptime(result['sunsetTime'], "%H:%M:%S"))

    # Normalize now for comparison (same dummy date)
    now_dummy = now.replace(year=1900, month=1, day=1)
    sunrise = sunrise.replace(year=1900, month=1, day=1)
    sunset = sunset.replace(year=1900, month=1, day=1)

    is_day = sunrise <= now_dummy <= sunset

    formatted_time = now.strftime("%I:%M %p")
    formatted_date = now.strftime("%A, %d %B")
    template = 'cityDay.html' if is_day else 'cityNight.html'

    return render_template(template, weather=result, time=formatted_time, date=formatted_date)


@app.route('/error')
def error():
    errorCode = request.args.get("errorCode", default="Unknown")
    errorMessage = request.args.get("errorMessage", default="Something went wrong.")
    return render_template('error.html', errorCode=errorCode, errorMessage=errorMessage)

@app.route('/usage')
def usage():
    return render_template('usage.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


if __name__ == "__main__":
    app.run(debug=True)
