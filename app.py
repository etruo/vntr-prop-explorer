from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import googlemaps
from geopy.geocoders import Nominatim
import folium
import requests
from bs4 import BeautifulSoup
import re
import json

load_dotenv()

app = Flask(__name__)

# Initialize Google Maps client
google_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
gmaps = googlemaps.Client(key=google_api_key) if google_api_key else None
geolocator = Nominatim(user_agent="kansas_property_lookup")

@app.route('/')
def index():
    """Main page with address input and results."""
    return render_template('index.html')

@app.route('/api/autocomplete')
def autocomplete():
    """Get address suggestions from Google Places API."""
    query = request.args.get('query', '')
    
    if not query or len(query) < 3:
        return jsonify([])
    
    suggestions = []
    
    if gmaps:
        try:
            # Search for places in Kansas
            places_result = gmaps.places_autocomplete(
                input_text=f"{query}, Kansas",
                types=['address'],
                session_token=None
            )
            
            for place in places_result[:5]:
                place_details = gmaps.place(place['place_id'], fields=['formatted_address'])
                if place_details.get('result'):
                    address = place_details['result'].get('formatted_address', '')
                    if 'KS' in address or 'Kansas' in address:
                        suggestions.append(address)
                        
        except Exception as e:
            print(f"Google Places API error: {e}")
    
    # Fallback to sample suggestions if no Google results
    if not suggestions:
        sample_addresses = [
            f"{query} Main St, Wichita, KS",
            f"{query} Oak Ave, Kansas City, KS",
            f"{query} Pine Rd, Overland Park, KS"
        ]
        suggestions = sample_addresses[:3]
    
    return jsonify(suggestions)

@app.route('/api/lookup')
def lookup_property():
    """Look up property details by address."""
    address = request.args.get('address', '')
    
    if not address:
        return jsonify({'error': 'Address required'})
    
    try:
        # Get coordinates
        location = geolocator.geocode(address)
        if not location:
            return jsonify({'error': 'Address not found'})
        
        coordinates = [location.latitude, location.longitude]
        
        # Get property details (mock data for now)
        property_data = get_property_details(address, coordinates)
        
        # Create map
        map_html = create_property_map(coordinates, address, property_data)
        
        return jsonify({
            'success': True,
            'property': property_data,
            'map': map_html
        })
        
    except Exception as e:
        return jsonify({'error': f'Lookup failed: {str(e)}'})

def get_property_details(address, coordinates):
    """Get property details from Sedgwick County website (mock for now)."""
    # This would be replaced with actual Sedgwick County scraping
    # For now, return mock data based on address hash
    
    import hashlib
    address_hash = hashlib.md5(address.encode()).hexdigest()
    
    # Generate consistent mock data based on address
    seed = int(address_hash[:8], 16)
    import random
    random.seed(seed)
    
    return {
        'address': address,
        'unit_type': 'Single Family',
        'sqft': random.randint(1200, 3000),
        'lot_size': random.randint(5000, 15000),
        'county_appraisal': random.randint(150000, 400000),
        'coordinates': coordinates
    }

def create_property_map(coordinates, address, property_data):
    """Create a Folium map showing the property location."""
    m = folium.Map(
        location=coordinates,
        zoom_start=15,
        tiles='OpenStreetMap'
    )
    
    # Add property marker
    popup_html = f"""
    <div style="font-family: Arial, sans-serif; min-width: 200px;">
        <h4 style="margin: 0 0 10px 0; color: #1f77b4;">🏠 {address}</h4>
        <p style="margin: 5px 0;"><strong>Unit Type:</strong> {property_data['unit_type']}</p>
        <p style="margin: 5px 0;"><strong>Square Feet:</strong> {property_data['sqft']:,}</p>
        <p style="margin: 5px 0;"><strong>Lot Size:</strong> {property_data['lot_size']:,} sq ft</p>
        <p style="margin: 5px 0;"><strong>County Appraisal:</strong> ${property_data['county_appraisal']:,}</p>
    </div>
    """
    
    folium.Marker(
        coordinates,
        popup=folium.Popup(popup_html, max_width=300),
        icon=folium.Icon(color='red', icon='home', prefix='fa'),
        tooltip="Property Location"
    ).add_to(m)
    
    return m._repr_html_()

if __name__ == '__main__':
    app.run(debug=True) 