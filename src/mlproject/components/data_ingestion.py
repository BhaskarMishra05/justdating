import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from mlproject.exception import CustomException

from mlproject.logger import logging

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'StudentsPerformance.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self) -> tuple:
        try:
            # Make sure artifacts folder exists
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Read the raw CSV file from artifacts (assume user placed it there)
            df = pd.read_csv(self.ingestion_config.raw_data_path)
            logging.info(f"Raw data loaded from {self.ingestion_config.raw_data_path}")

            # Split into train and test
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the train/test splits
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info(f"Train data saved to {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved to {self.ingestion_config.test_data_path}")
            logging.info("Data ingestion completed successfully.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
