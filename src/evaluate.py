from pathlib import Path
import sys
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import joblib
import dvclive


def evaluate(clf, X_test, y_test):
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="macro")
    recall = recall_score(y_test, y_pred, average="macro")
    f1 = f1_score(y_test, y_pred, average="macro")

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}


if __name__ == "__main__":
    data_directory = Path(sys.argv[1])

    absolute_data_directory = data_directory.resolve()

    X_test = pd.read_pickle(absolute_data_directory / "prepared" / "X_test.pkl")
    y_test = pd.read_pickle(absolute_data_directory / "prepared" / "y_test.pkl")

    clf = joblib.load(absolute_data_directory / "models" / "model.pkl")

    metrics = evaluate(clf, X_test, y_test)

    with dvclive.Live() as live:
        for metric, value in metrics.items():
            live.log_metric(metric, value)
