from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation

# Load data
ingestor = DataIngestion()
df = ingestor.load_data()
print(df.head())

# Transform data
transformer = DataTransformation()
X, y = transformer.transform(df)
print("Features shape:", X.shape)
print("Labels shape:", y.shape)