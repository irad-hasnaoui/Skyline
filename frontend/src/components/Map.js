import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import axios from 'axios';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const MapComponent = ({ city, latitude, longitude }) => {
  const [weatherData, setWeatherData] = useState(null);

  useEffect(() => {
    if (latitude && longitude) {
      // Fetch weather data for the latitude and longitude
      axios
        .get(`/weather?lat=${latitude}&lon=${longitude}`)
        .then((response) => setWeatherData(response.data))
        .catch((error) => console.error('Error fetching weather data:', error));
    }
  }, [latitude, longitude]);

  return (
    <MapContainer center={[latitude, longitude]} zoom={10} style={{ width: '100%', height: '400px' }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      <Marker position={[latitude, longitude]} icon={new L.Icon({ iconUrl: 'https://upload.wikimedia.org/wikipedia/commons/a/a1/Weather_icon_1.png', iconSize: [32, 32] })}>
        <Popup>
          <h2>{weatherData?.city}</h2>
          <p>Temperature: {weatherData?.temperature}°C</p>
          <p>Description: {weatherData?.description}</p>
          <p>Humidity: {weatherData?.humidity}%</p>
          <p>Wind Speed: {weatherData?.wind_speed} m/s</p>
        </Popup>
      </Marker>
    </MapContainer>
  );
};

export default MapComponent;
