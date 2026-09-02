import pandas as pd


def Read_data_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except PermissionError:
        print("The file cannot be read. Please check the file permission.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty.")
        return None
    except pd.errors.ParserError:
        print("The file format is not valid CSV.")
        return None
    except Exception as error:
        print("Error while reading the file:", error)
        return None


def Drop_unnecessary_features(df, cols_to_drop):
    return df.drop(columns=cols_to_drop, errors="ignore")


def Check_data_type(df):
    report = pd.DataFrame({
        "Data Type": df.dtypes,
        "Unique Values": df.nunique()
    })

    return report.T
