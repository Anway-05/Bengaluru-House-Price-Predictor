import os
import joblib
import json
import pandas as pd

__model = None
__locations = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_saved_artifacts():
    global __model
    global __locations

    if __model is None:
        print("Loading model...")

        model_path = os.path.join(
            BASE_DIR,
            "..",
            "Model",
            "Bengaluru_housing_prices_project_model"
        )

        __model = joblib.load(model_path)

    if __locations is None:
        print("Loading locations...")

        locations_path = os.path.join(
            BASE_DIR,
            "..",
            "Model",
            "locations.json"
        )

        with open(locations_path, "r") as f:
            __locations = json.load(f)

    print("Loading saved artifacts...done")


def get_location_names():
    return __locations


def get_estimated_price(location, sqft, bath, balcony, bhk):

    input_df = pd.DataFrame({
        "location": [location],
        "total_sqft": [float(sqft)],
        "bath": [float(bath)],
        "balcony": [float(balcony)],
        "bhk": [int(bhk)]
    })

    prediction = __model.predict(input_df)[0]

    return round(prediction, 2)


if __name__ == "__main__":
    load_saved_artifacts()

    print(get_location_names()[:10])

    print(
        get_estimated_price(
            "Whitefield",
            1500,
            2,
            1,
            3
        )
    )