# DVC Template

This project aims to showcase the usage of dvc in ML project to enhance reproducibility.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: You need Python installed on your machine. Python 3.8 or higher is recommended. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Ensure that pip is installed. pip usually comes with Python, but if you don't have it, you can install it by following the instructions [here](https://pip.pypa.io/en/stable/installing/).
- **DVC**: Data Version Control (DVC) needs to be installed. You can install it using pip. For more details on installation, visit the [official DVC installation guide](https://dvc.org/doc/install).

## Additional dependencies

Installation of [DVC IDE plugins](https://dvc.org/doc/install/ide-plugins) is recommended, but not necessary.

## Installation

To set up your local development environment, follow these steps:

1. Create the virtual environment and install the required Python packages:

```bash
pip install -r src/requirements.txt
```

2. Execute the dvc pipeline

```bash
dvc repro
```
