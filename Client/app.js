function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");

    for (var i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1;
}


function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");

    for (var i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}


function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://10.202.95.11:5000/predict_home_price";

    $.post(url, {
        total_sqft: parseFloat(sqft),
        bhk: bhk,
        bath: bathrooms,
        balcony: 1,
        location: location
    })
    .done(function(data) {
        console.log(data);

        estPrice.innerHTML =
            "<h2>" + data.estimated_price + " Lakh</h2>";
    })
    .fail(function() {
        estPrice.innerHTML =
            "<h2 style='color:red;'>Server Error / Not Connected</h2>";
    });
}


function onPageLoad() {
    console.log("document loaded");

    var url = "http://10.202.95.11:5000/get_location_names";

    $.get(url)
    .done(function(data) {
        console.log("got response for location request");

        if (data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");

            $('#uiLocations').empty();

            for (var i = 0; i < locations.length; i++) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    })
    .fail(function() {
        console.log("Failed to load locations");
    });
}

window.onload = onPageLoad;