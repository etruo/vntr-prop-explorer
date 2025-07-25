#!/usr/bin/env python3
"""
Simple test for the Flask property lookup app.
"""

import requests
import json

def test_autocomplete():
    """Test the autocomplete API endpoint."""
    print("🧪 Testing Autocomplete API...")
    
    # Test with a sample query
    response = requests.get('http://localhost:5000/api/autocomplete?query=1901')
    
    if response.status_code == 200:
        suggestions = response.json()
        print(f"✅ Autocomplete working - found {len(suggestions)} suggestions")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"   {i}. {suggestion}")
    else:
        print(f"❌ Autocomplete failed - status code: {response.status_code}")

def test_lookup():
    """Test the property lookup API endpoint."""
    print("\n🧪 Testing Property Lookup API...")
    
    # Test with a sample address
    test_address = "1901 N Paddock Green St, Wichita, KS"
    response = requests.get(f'http://localhost:5000/api/lookup?address={test_address}')
    
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            property_data = data['property']
            print("✅ Property lookup successful!")
            print(f"   Address: {property_data['address']}")
            print(f"   Unit Type: {property_data['unit_type']}")
            print(f"   Square Feet: {property_data['sqft']:,}")
            print(f"   Lot Size: {property_data['lot_size']:,} sq ft")
            print(f"   County Appraisal: ${property_data['county_appraisal']:,}")
            print(f"   Coordinates: {property_data['coordinates']}")
            print("   Map HTML generated successfully")
        else:
            print(f"❌ Property lookup failed: {data.get('error')}")
    else:
        print(f"❌ Property lookup failed - status code: {response.status_code}")

def main():
    """Run the tests."""
    print("🚀 Testing Kansas Property Lookup App...\n")
    
    try:
        test_autocomplete()
        test_lookup()
        print("\n🎉 All tests completed!")
        print("💡 The app is ready for deployment to Vercel")
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to app. Make sure it's running on localhost:5000")
        print("   Run: python app.py")
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")

if __name__ == "__main__":
    main() 