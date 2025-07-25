# Deployment Guide for Vercel

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Repository**: Push your code to GitHub
3. **Google Maps API Key**: Get one from [Google Cloud Console](https://console.cloud.google.com)

## Deployment Steps

### 1. Connect to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your GitHub repository
4. Select the repository containing this code

### 2. Configure Environment Variables

In the Vercel dashboard:

1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add the following variable:
   - **Name**: `GOOGLE_MAPS_API_KEY`
   - **Value**: Your Google Maps API key
   - **Environment**: Production, Preview, Development

### 3. Deploy

1. Vercel will automatically detect this is a Python project
2. The `vercel.json` file configures the deployment
3. Click "Deploy" and wait for the build to complete

### 4. Verify Deployment

1. Your app will be available at `https://your-project-name.vercel.app`
2. Test the autocomplete functionality
3. Test the property lookup feature

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export GOOGLE_MAPS_API_KEY=your_api_key_here

# Run locally
python app.py

# Test the app
python test_app.py
```

## Troubleshooting

### Common Issues

1. **Build Fails**: Check that all dependencies are in `requirements.txt`
2. **API Errors**: Verify your Google Maps API key is correct
3. **CORS Issues**: The app should work without CORS configuration

### Environment Variables

Make sure your Google Maps API key:

- Has the Places API enabled
- Has billing set up (required for Places API)
- Is correctly set in Vercel environment variables

## Next Steps

After deployment, you can:

1. **Add Custom Domain**: Configure a custom domain in Vercel settings
2. **Monitor Performance**: Use Vercel analytics to track usage
3. **Implement Real Data**: Replace mock data with Sedgwick County scraping
4. **Add More Counties**: Expand to other Kansas counties
