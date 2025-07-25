# Kansas Property Lookup

A simple web application for looking up property details in Kansas using Google Places API for address autocomplete.

## Features

- **Address Autocomplete**: Google Places API integration for real-time address suggestions
- **Property Details**: Unit type, square footage, lot size, and county appraisal
- **Interactive Map**: Visual location display using Folium maps
- **Clean UI**: Modern, responsive design with Bootstrap

## Setup

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   Create a `.env` file with:

   ```
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
   ```

3. **Run locally**:

   ```bash
   python app.py
   ```

4. **Deploy to Vercel**:
   - Connect your GitHub repository to Vercel
   - Add environment variables in Vercel dashboard
   - Deploy automatically

## API Endpoints

- `GET /` - Main application page
- `GET /api/autocomplete?query=<address>` - Get address suggestions
- `GET /api/lookup?address=<address>` - Look up property details

## Current Status

- ✅ Google Places API autocomplete
- ✅ Property details (mock data)
- ✅ Interactive map display
- ⏳ Sedgwick County website scraping (TODO)

## Next Steps

1. Implement Sedgwick County website scraping for real appraisal data
2. Add error handling for bot protection
3. Expand to other Kansas counties
4. Add property history and trends

## Tech Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Maps**: Folium
- **APIs**: Google Places API, Geopy
- **Deployment**: Vercel
