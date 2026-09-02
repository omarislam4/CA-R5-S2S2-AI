from config.config import dataset, DROP_COLUMNS
from src.components.data_preprocessing import (
    Read_data_file,
    Drop_unnecessary_features,
    Check_data_type
)


def run_pipeline():
    df = Read_data_file(dataset)

    if df is None:
        return None

    print("Dataset loaded successfully")
    print("Shape:", df.shape)

    print("\nData types and unique values:")
    print(Check_data_type(df))

    df = Drop_unnecessary_features(df, DROP_COLUMNS)

    print("\nColumns after removing unnecessary features:")
    print(df.columns.tolist())

    print("\nData types after preprocessing:")
    print(Check_data_type(df))

    return df
