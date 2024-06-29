import tkinter as tk
import requests

def get_top_places(latitude, longitude, category):
    url = f"https://api.opentripmap.com/0.1/en/places/radius?radius=10000&lon={longitude}&lat={latitude}&kinds={category}&limit=10&apikey=YOUR_API_KEY"
    try:
        response = requests.get(url)
        data = response.json()
        top_places = [(place['name'], place['dist']) for place in data]
        return top_places
    except Exception as e:
        return None

def show_results():
    latitude = latitude_entry.get()
    longitude = longitude_entry.get()
    category = category_entry.get()

    if latitude and longitude and category:
        top_places = get_top_places(latitude, longitude, category)
        if top_places:
            result_text.delete('1.0', tk.END)
            for i, place in enumerate(top_places, 1):
                result_text.insert(tk.END, f"{i}. {place[0]} - Distance: {place[1]} meters\n")
        else:
            result_text.delete('1.0', tk.END)
            result_text.insert(tk.END, "Error fetching data. Please try again later.")
    else:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "Please provide latitude, longitude, and category.")

# Create main window
root = tk.Tk()
root.title("Top 10 Visitable Places Finder")

# Latitude Frame
latitude_frame = tk.Frame(root)
latitude_frame.pack(padx=20, pady=10)

latitude_label = tk.Label(latitude_frame, text="Latitude:")
latitude_label.grid(row=0, column=0, padx=5, pady=5)
latitude_entry = tk.Entry(latitude_frame)
latitude_entry.grid(row=0, column=1, padx=5, pady=5)

# Longitude Frame
longitude_frame = tk.Frame(root)
longitude_frame.pack(padx=20, pady=10)

longitude_label = tk.Label(longitude_frame, text="Longitude:")
longitude_label.grid(row=0, column=0, padx=5, pady=5)
longitude_entry = tk.Entry(longitude_frame)
longitude_entry.grid(row=0, column=1, padx=5, pady=5)

# Category Frame
category_frame = tk.Frame(root)
category_frame.pack(padx=20, pady=10)

category_label = tk.Label(category_frame, text="Category:")
category_label.grid(row=0, column=0, padx=5, pady=5)
category_entry = tk.Entry(category_frame)
category_entry.grid(row=0, column=1, padx=5, pady=5)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack(padx=20, pady=10)

search_button = tk.Button(button_frame, text="Search", command=show_results)
search_button.pack(padx=5, pady=5)

# Result Frame
result_frame = tk.Frame(root)
result_frame.pack(padx=20, pady=10)

result_label = tk.Label(result_frame, text="Top 10 Places:")
result_label.pack(padx=5, pady=5)

result_text = tk.Text(result_frame, height=10, width=50)
result_text.pack(padx=5, pady=5)

root.mainloop()