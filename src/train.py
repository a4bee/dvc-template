import logging
from pathlib import Path
import sys
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

import pandas as pd
import dvc.api

import joblib


logging.basicConfig(level=logging.INFO)


clfs = [
    MLPClassifier(alpha=1, max_iter=1000, random_state=42),
    AdaBoostClassifier(algorithm="SAMME", random_state=42),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
]


def train(seed, clf_index, X_train, y_train, params):
    clf = clfs[clf_index]

    if params:
        clf.set_params(**params)

    clf.fit(X_train, y_train)
    logging.info(
        f"Classifier {clf.__class__.__name__} trained with seed {seed} and parameters {params}"
    )

    return clf


if __name__ == "__main__":
    data_directory = Path(sys.argv[1])

    absolute_data_directory = data_directory.resolve()

    X_train = pd.read_pickle(absolute_data_directory / "prepared" / "X_train.pkl")
    y_train = pd.read_pickle(absolute_data_directory / "prepared" / "y_train.pkl")

    params = dvc.api.params_show()["train"]

    clf = train(
        params["seed"], params["clf"], X_train, y_train, params.get("clf_params", {})
    )

    models_directory = absolute_data_directory / "models"

    models_directory.mkdir(parents=True, exist_ok=True)

    joblib.dump(clf, absolute_data_directory / "models" / "model.pkl")
