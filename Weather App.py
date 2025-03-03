import requests
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import io

# Function to fetch weather data
def get_weather(city):
    api_key = "c051565e1fd7f35d124271b716c456a4"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return None

# Function to update weather details dynamically
def fetch_weather(event=None):
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    data = get_weather(city)
    if data and data["cod"] == 200:
        weather_desc = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        
        icon_response = requests.get(icon_url)
        if icon_response.status_code == 200:
            img_data = icon_response.content
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((60, 60), Image.LANCZOS)  # Smaller icon size
            weather_icon = ImageTk.PhotoImage(img)
            icon_label.config(image=weather_icon)
            icon_label.image = weather_icon
        
        result_label.config(text=f"{data['name']}", font=("Arial", 12, "bold"), fg="white")
        temp_label.config(text=f"{temp}°C", font=("Arial", 14, "bold"), fg="#FF5733")
        humidity_label.config(text=f"Humidity: {humidity}%", font=("Arial", 10), fg="#33A1FF")
        weather_desc_label.config(text=f"{weather_desc}", font=("Arial", 10, "bold"), fg="yellow")
        wind_label.config(text=f"Wind: {wind_speed} m/s", font=("Arial", 10), fg="#FFC107")
        update_background(weather_desc)
    else:
        result_label.config(text="City not found", font=("Arial", 10), fg="red")

# Function to update background and effects based on weather conditions
def update_background(weather_desc):
    if "sunny" in weather_desc.lower():
        app.configure(bg="#222222")  # Darker Sun Mode
    elif "cloud" in weather_desc.lower():
        app.configure(bg="#555555")  # Cloudy Grey
    elif "rain" in weather_desc.lower():
        app.configure(bg="#003366")  # Rainy Blue
    elif "wind" in weather_desc.lower():
        app.configure(bg="#777777")  # Windy Grey
    else:
        app.configure(bg="#1E1E1E")

# GUI Setup
app = Tk()
app.title("Weather App")
app.geometry("250x250")  # Compact size
app.configure(bg="#1E1E1E")

frame = Frame(app, bg="#333333", bd=3)
frame.pack(pady=5, padx=5, fill=X)

Label(frame, text="City:", font=("Arial", 10, "bold"), bg="#333333", fg="white").pack(side=LEFT, padx=5)
city_entry = Entry(frame, font=("Arial", 10))
city_entry.pack(side=LEFT, padx=5)
city_entry.bind("<Return>", fetch_weather)  # Press Enter to fetch weather

Button(frame, text="Get", font=("Arial", 10, "bold"), command=fetch_weather, bg="#444444", fg="white").pack(side=LEFT, padx=5)

icon_label = Label(app, bg="#1E1E1E")
icon_label.pack(pady=5)

result_label = Label(app, text="", bg="#1E1E1E", fg="white")
result_label.pack()

temp_label = Label(app, text="", bg="#1E1E1E", fg="white")
temp_label.pack()

humidity_label = Label(app, text="", bg="#1E1E1E", fg="white")
humidity_label.pack()

weather_desc_label = Label(app, text="", bg="#1E1E1E", fg="white")
weather_desc_label.pack()

wind_label = Label(app, text="", bg="#1E1E1E", fg="white")
wind_label.pack()

app.mainloop()
