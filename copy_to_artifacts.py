import os
import shutil

source_path= '/home/bhaskar/Downloads/StudentsPerformance.csv'
 
destination_path= os.path.join('artifacts','StudentsPerformance.csv')

os.makedirs('artifacts',exist_ok=True)

try:
    shutil.copy(source_path, destination_path)
    print(f"File copied to {destination_path}")
except Exception as e:
    print(f"Error: {e}")