import zipfile

with zipfile.ZipFile("data/students-performance-dataset.zip", "r") as zip_ref:
    zip_ref.extractall("./data")
