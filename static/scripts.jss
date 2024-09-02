function getLocationWeather() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            fetch('/location_weather', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    alert('Weather data fetched based on location. Check console for details.');
                    console.log(data);
                }
            })
            .catch(error => {
                alert('An error occurred while fetching weather data.');
                console.error(error);
            });
        });
    } else {
        alert('Geolocation is not supported by this browser.');
    }
}
