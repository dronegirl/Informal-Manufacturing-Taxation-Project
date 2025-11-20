import pandas as pd
import folium
from folium.plugins import HeatMap

# Load your CSV data
data = pd.read_csv('your_file.csv')

# Print column names to verify latitude and longitude
print(data.columns.tolist())

# Create heat data with correct column names
heat_data = [[row['latitude'], row['longitude']] for index, row in data.iterrows()]

# Create a base map
m = folium.Map(location=[-17.8292, 31.0522], zoom_start=12)

# Add the heatmap layer
HeatMap(heat_data).add_to(m)

# Save the map to an HTML file
output_file = 'density_heatmap.html'
m.save(output_file)

# Output file confirmation
print(f'Map has been saved to {output_file}. Open this file in a web browser to view the heatmap.')