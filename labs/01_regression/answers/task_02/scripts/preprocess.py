# pylint: disable=missing-docstring
from pathlib import Path

import pandas as pd
from lab01.config import DATA_DIR
from lab01.dataloader import load_housing_data
from lab01.preprocess import preprocess_data


def save_preprocessed_data(data: pd.DataFrame, output_dir: Path) -> None:
    '''Saves the pre-processed California Housing Prices dataset to the output directory.
    
    Args:
        data: A pandas DataFrame containing the pre-processed California Housing Prices dataset.
        output_dir: The output directory.
    '''
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / 'preprocessed_data.csv'
    data.to_csv(output_path, index=False)


def main():
    data = load_housing_data(DATA_DIR)
    preprocessed_data = preprocess_data(data)
    save_preprocessed_data(preprocessed_data, DATA_DIR)


if __name__ == '__main__':
    main()
