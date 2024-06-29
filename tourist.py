import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
import requests

def get_coordinates_and_places():
    location_name = location_entry.get()
    geolocator = Nominatim(user_agent="location_finder")
    
    try:
        location = geolocator.geocode(location_name)
        if location:
            latitude = location.latitude
            longitude = location.longitude
            coordinates_label.config(text=f"Coordinates: {latitude}, {longitude}")
            top_places = get_top_places(latitude, longitude)
            display_places(top_places)
        else:
            messagebox.showerror("Error", "Location not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def get_top_places(latitude, longitude):
    # OpenTripMap API endpoint for tourist attractions
    url = 'https://api.opentripmap.com/0.1/en/places/radius'
    
    # Free API key (limited usage)
    api_key = '5ae2e3f221c38a28845f05b669b3b79fcb06247f5585330045816bb7'
    
    # Parameters for the API request
    params = {
        'apikey': api_key,
        'radius': 10000,  # Search radius in meters
        'limit': 15,  # Limit to top 10 places
        'lon': longitude,
        'lat': latitude
    }
    
    try:
        # Sending GET request to OpenTripMap API
        response = requests.get(url, params=params)
        data = response.json()
        
        # Extracting top places
        top_places = []
        for place in data['features']:
            place_name = place['properties']['name']
            place_distance = place['properties']['dist']
            top_places.append((place_name, place_distance))
        
        return top_places
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while fetching places: {str(e)}")

def display_places(places):
    places_text.delete('1.0', tk.END)
    for i, place in enumerate(places, 1):
        places_text.insert(tk.END, f"{i}. {place[0]} - Distance: {place[1]} meters\n")

# Create main window
root = tk.Tk()
root.title("Tourist Places Finder")

# Location Frame
location_frame = tk.Frame(root)
location_frame.pack(padx=20, pady=20)

# Location Label and Entry
location_label = tk.Label(location_frame, text="Enter Location:")
location_label.grid(row=0, column=0, padx=5, pady=5)
location_entry = tk.Entry(location_frame)
location_entry.grid(row=0, column=1, padx=5, pady=5)

# Get Places Button
get_places_button = tk.Button(location_frame, text="Get Places", command=get_coordinates_and_places)
get_places_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Coordinates Label
coordinates_label = tk.Label(root, text="")
coordinates_label.pack(padx=20, pady=10)

# Places Text
places_text = tk.Text(root, height=15, width=50)
places_text.pack(padx=20, pady=10)

root.mainloop()