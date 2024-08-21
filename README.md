# Scraping-Billboard-100
# Billboard to Spotify Playlist Creator

This project is a Python script that scrapes the Billboard Hot 100 chart for a specified date and creates a Spotify playlist with the top songs from that chart. The application uses BeautifulSoup for web scraping and Spotipy for interacting with the Spotify API.

## Features

- Scrapes the Billboard Hot 100 chart for a specific date
- Automatically searches for the songs on Spotify
- Creates a private playlist on your Spotify account with the found songs

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine
- A Spotify account
- Registered a Spotify application and obtained a client ID and client secret from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/billboard-spotify-playlist.git
   cd billboard-spotify-playlist
2. Install the required Python packages:
 ```bash
   pip install requests beautifulsoup4 spotipy
```
3. Set up your Spotify application credentials in the script:
   ```bash
   client_id = 'your_client_id'
   client_secret = 'your_client_secret'
   redirect_uri = 'http://example.com'  # The redirect URI you set up in the Spotify Developer Dashboard

## Usage
1. Run the script:
   ```bash
   python main.py

2. Enter the date in YYYY-MM-DD format when prompted.
3. The script will create a private Spotify playlist on your account with the top songs from the Billboard Hot 100 chart on the specified date.

## Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

Screenshot
