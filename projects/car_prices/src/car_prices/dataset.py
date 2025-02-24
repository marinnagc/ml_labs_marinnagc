'''Module for loading the car dataset.
'''
import zipfile
from pathlib import Path

import pandas as pd
import requests

_CAR_DATASET_URL = 'https://www.kaggle.com/api/v1/datasets/download/asinow/car-price-dataset'
_TIMEOUT = 10
_PROJECT_NAME = 'car_price'
_COMPRESSED_CAR_DATASET_FILENAME = 'car_price_dataset.zip'
_CAR_DATASET_FILENAME = 'car_price_dataset.csv'


def _fetch_car_dataset(raw_dataset_path: Path, project_data_dir: Path) -> None:
    '''Fetches the car dataset from Kaggle and saves it to the data_dir.
    '''
    project_data_dir.mkdir(parents=True, exist_ok=True)
    response = requests.get(_CAR_DATASET_URL, timeout=_TIMEOUT)
    response.raise_for_status()
    with open(raw_dataset_path, 'wb') as f:
        f.write(response.content)


def _unpack_car_dataset(raw_dataset_path: Path, project_data_dir: Path) -> None:
    '''Unpacks the car dataset from the data_dir.
    '''
    with zipfile.ZipFile(raw_dataset_path, 'r') as zip_ref:
        zip_ref.extractall(project_data_dir)


def _fetch_and_unpack_car_dataset(project_data_dir: Path) -> None:
    '''Fetches and unpacks the car dataset from Kaggle.
    '''
    raw_dataset_path = project_data_dir / _COMPRESSED_CAR_DATASET_FILENAME
    _fetch_car_dataset(raw_dataset_path, project_data_dir)
    _unpack_car_dataset(raw_dataset_path, project_data_dir)


def load_car_dataset(data_dir: str | Path) -> pd.DataFrame:
    '''Loads the car dataset from the data_dir.
    '''
    data_dir = Path(data_dir)
    project_data_dir = data_dir / _PROJECT_NAME
    dataset_path = project_data_dir / _CAR_DATASET_FILENAME
    if not dataset_path.exists():
        _fetch_and_unpack_car_dataset(project_data_dir)
    dataset = pd.read_csv(dataset_path)
    return dataset
