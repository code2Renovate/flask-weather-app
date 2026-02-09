# 🌦️ Flask Weather App

A modern, responsive **Weather Web Application** built using **Flask**, **HTML**, **CSS**, and **Bootstrap**.  
The app fetches real-time weather data and dynamically switches between **Day Mode** and **Night Mode** based on the local time of the searched city.

---

## 🚀 Features

- 🌍 Search weather by city name
- 🏙️ Default weather displayed for **Patna**
- ☀️ **Day Mode UI** based on city local daytime
- 🌙 **Night Mode UI** based on city local nighttime
- ⏱️ Real-time weather details:
  - Temperature
  - Feels-like temperature
  - Humidity
  - Wind speed
  - Atmospheric pressure
  - Sunrise & sunset time
- ❌ **Custom error handling page** for invalid input or API failure
- 📱 Fully responsive design using Bootstrap

---

## 🖼️ Screenshots

### 🏠 Home Page (Default – Patna Weather)
Displays default weather for **Patna** with a search bar.

![Home Page](https://github.com/user-attachments/assets/7a07538c-958f-40fe-9e3e-5dc2298d7c6b)

---

### ☀️ Day Mode
Automatically activated when it is daytime at the searched location.

![Day Mode](https://github.com/user-attachments/assets/b3f49a15-e9f9-49f1-a864-8ff8253dbd43)

---

### 🌙 Night Mode
Displayed when it is nighttime at the searched location.

![Night Mode](https://github.com/user-attachments/assets/a399d1ad-6d05-4c6d-ab57-86887d567e54)

---

### ⚠️ Error Handling Page
Shown when an invalid city is entered or the API request fails.

![Error Page](https://github.com/user-attachments/assets/00a850fe-8520-4eac-9839-481caf782820)

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML5
- CSS3
- Bootstrap

### API
- Visual Crossing Weather API (real-time weather data)

---

## 📂 Project Structure

```text
WEATHER-APP-PROJECT/
│
├── static/
│   ├── css/
│   ├── images/
│   └── bootstrap files
│
├── templates/
│   ├── index.html
│   ├── cityDay.html
│   ├── cityNight.html
│   ├── error.html
│   ├── privacy.html
│   └── usage.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/code2Renovate/flask-weather-app.git
cd flask-weather-app
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment
- Windows
```bash
venv\Scripts\activate
```
- Mac / Linux
```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Get your free Visual Crossing API key
- 1. Go to [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api)
- 2. Sign up for a free account
- 3. Copy your API key
 
### 6️⃣ Add your API key
- Open app.py
- Replace the placeholder in this line:
- API_KEY = "<YOUR_API_KEY>"
- Paste your API key between the quotes.

### 7️⃣ Run the application
```bash
python app.py
```

### 8️⃣ Open your browser and visit:
```bash
http://127.0.0.1:5000/
```
