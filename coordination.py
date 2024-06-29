import tkinter as tk
from geopy.geocoders import Nominatim

def get_coordinates():
    location_name = location_entry.get()
    geolocator = Nominatim(user_agent="location_finder")
    try:
        location = geolocator.geocode(location_name)
        if location:
            latitude = location.latitude
            longitude = location.longitude
            result_label.config(text=f"Latitude: {latitude}\nLongitude: {longitude}")
        else:
            result_label.config(text="Location not found.")
    except Exception as e:
        result_label.config(text="Error occurred while fetching coordinates.")

# Create main window
root = tk.Tk()
root.title("Location Coordinates Finder")

# Location Frame
location_frame = tk.Frame(root)
location_frame.pack(padx=20, pady=20)

# Location Label and Entry
location_label = tk.Label(location_frame, text="Enter Location:")
location_label.grid(row=0, column=0, padx=5, pady=5)
location_entry = tk.Entry(location_frame)
location_entry.grid(row=0, column=1, padx=5, pady=5)

# Get Coordinates Button
get_coordinates_button = tk.Button(location_frame, text="Get Coordinates", command=get_coordinates)
get_coordinates_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(padx=20, pady=10)

root.mainloop()
