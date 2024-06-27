import pandas as pd
import sys
import logging
import dvc.api
from pathlib import Path
from sklearn.model_selection import train_test_split

def main():
    # Get the path to the data file from the command line argument
    data_file_path = Path(sys.argv[1])
    absolute_data_file_path = data_file_path.resolve()

    data_directory = absolute_data_file_path.parent

    logging.info(f"Reading file {absolute_data_file_path}")

    df = pd.read_csv(absolute_data_file_path)

    params = dvc.api.params_show()
    seed = params['prepare']['seed']
    split = params['prepare']['split']

    X = df.drop(columns='GradeClass')
    y = df['GradeClass']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split, stratify=y, random_state=seed)

    prepared_directory = data_directory / "prepared"
    prepared_directory.mkdir(parents=True, exist_ok=True)

    pd.to_pickle(X_train, prepared_directory / "X_train.pkl")
    pd.to_pickle(y_train, prepared_directory / "y_train.pkl")
    pd.to_pickle(X_test, prepared_directory / "X_test.pkl")
    pd.to_pickle(y_test, prepared_directory / "y_test.pkl")

    logging.info(f"Prepared data saved to {prepared_directory}")

if __name__ == "__main__":
    main()
