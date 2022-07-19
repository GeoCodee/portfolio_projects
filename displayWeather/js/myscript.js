//Get current location
$(function () {
  if (navigator.geolocation) {
    var configOptions = {
      enableHighAccuracy: true,
      timeout: 5000,
      maximumAge: 0,
    };

    navigator.geolocation.getCurrentPosition(
      onLocationSuccess,
      onLocationError,
      configOptions
    );
  } else {
    console.log("Geolocation cannot be accessed");
  }
});

function onLocationSuccess(location) {
  console.log(`Current location received: ${location}`);

  const lat = location.coords.latitude;
  const lng = location.coords.longitude;

  console.log(`Lat: - ${lat} Lng: ${lng}`);
  getWeatherInfo(lat, lng);
}

function onLocationError() {
  console.log(`Unable to get location ${error.code} ${error.message}`);
}

function getWeatherInfo(lat, lng) {
  const apiKey = "fc74df2160bbefadee19529c0aaa1bde";
  const apiURL = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${apiKey}`;

  console.log(apiURL);

  $.ajax({
    type: "GET",
    url: apiURL,
    dataType: "json",
    success: showWeather,
    error: function (e) {
      console.log(
        `Something went wrong while fetching the weather info ${e.message}`
      );
    },
  });
}

function showWeather(weather) {
  console.log(`Weather info ${weather}`);

  $(".dataCity").html(weather.name);
  $(".dataTemp").html(`${(weather.main.temp - 273.15).toFixed(0)} c`);
  $(".dataHum").html(`${weather.main.humidity}%`);
  $(".dataPress").html(`${weather.main.pressure} mbars`);
  $(".dataWind").html(`${weather.wind.speed} knots`);
}
// Get API key from https://home.openweathermap.org/
// var apiURL = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${apiKey}`;

/*
 The Kelvin scale is an absolute, thermodynamic temperature scale 
 using as its null point absolute zero, the temperature at which 
 all thermal motion ceases in the classical description of thermodynamics.
  To get Celsius, subtract 273.15 from Kelvin temp
*/

// clouds.all (%)
// main.humidity, pressure, temp
// name
// syst.country, sunrise, sunset
// weather[x].description
// wind.deg, speed
