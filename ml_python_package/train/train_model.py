import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression


def build_model(model_type: str):
    if model_type == "RandomForestRegressor":
        model = RandomForestClassifier(n_estimators=100, random_state=30)
    elif model_type == "LinearRegression":
        model = LinearRegression()
    else:
        raise RuntimeError(f"Bad model_type -- {model_type}")
    return model


def train_model(features: pd.DataFrame, target: pd.Series, model_type: str):
    model = build_model(model_type)
    model.fit(features, target)
    return model


def serialize_model(model: object, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output
