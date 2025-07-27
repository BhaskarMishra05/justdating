from src.mlproject.components.data_transformation import DataTransformation

# Initialize the class
transformer = DataTransformation()

# Give the correct path to your CSVs
TRAIN_CSV_PATH = 'artifacts/train.csv'
TEST_CSV_PATH = 'artifacts/test.csv'

# Call the function
train_array, test_array, model_path = transformer.initiation_data_transfromation(TRAIN_CSV_PATH, TEST_CSV_PATH)

print("Train shape:", train_array.shape)
print("Test shape:", test_array.shape)
print("Preprocessing object saved at:", model_path)
