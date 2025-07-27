import os
import sys
import pandas as pd
import numpy as np
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, SimpleImputer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
import joblib

@dataclass
class DataTransformationConfig:
    transformed_data_file_path= os.path.join('artifacts','preprocssed.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation= DataTransformationConfig()

    def data_transformation_obj_for_feature_engineering(self):
        try:
            numerical_columns = ["writing score", "reading score"]
            categorical_columns = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course",
            ]

            numerical_pipeline= Pipeline(steps=[('Imputer',IterativeImputer()),
                                                ('scaler', StandardScaler())])

            categorical_pipeline= Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')),
                                                  ('encoder',OneHotEncoder(drop='first',handle_unknown='error'))])


            logging.info(f"Numerical column {numerical_columns}")
            logging.info(f"Categorial column {categorical_columns}")


            preprocssor= ColumnTransformer([('num_pipeline', numerical_pipeline, numerical_columns),
                                            ('cat_pipeline', categorical_pipeline, categorical_columns)])
            
            return preprocssor
        except Exception as e:
            raise CustomException(e,sys)


    def initiation_data_transfromation(self, train_data, test_data):
        try:
                
            df_train = pd.read_csv(train_data)
            df_test = pd.read_csv(test_data)

            logging.info("Reading from train and test file ")

            preprocssing_obj = self.data_transformation_obj_for_feature_engineering()

            TARGET = 'math score'
            numerical_columns = ["writing score", "reading score"]

            FEATURES_TRAIN = df_train.drop(columns=[TARGET],axis=1)
            TARGET_TRAIN = df_train[TARGET]
            

            FEATURES_TEST = df_test.drop(columns=[TARGET],axis=1)
            TARGET_TEST = df_test[TARGET]

            logging.info("Applying preprocessing on train and test set ")

            PROCESSED_FEATURES_TRAIN_ARRAY  = preprocssing_obj.fit_transform(FEATURES_TRAIN)
            PROCESSED_FEATURES_TEST_ARRAY = preprocssing_obj.transform(FEATURES_TEST)

            TRAIN_ARRAY = np.c_[
                    PROCESSED_FEATURES_TRAIN_ARRAY, np.array(TARGET_TRAIN)
            ]

            TEST_ARRAY = np.c_[
                    PROCESSED_FEATURES_TEST_ARRAY, np.array(TARGET_TEST)
            ]

            logging.info(f" Saved {preprocssing_obj}")
            joblib.dump(preprocssing_obj, self.data_transformation.transformed_data_file_path)

            return TRAIN_ARRAY, TEST_ARRAY, self.data_transformation.transformed_data_file_path



        except Exception as e:
            raise CustomException(e,sys)