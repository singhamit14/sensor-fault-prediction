import os 

TARGET_COLUMN = "class"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR = "artifact"
FILE_NAME = "sensor.csv"


TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

PROCESSING_OBJECT_FILE_NAME = "processing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"

#  data ingestion related constants Value

DATA_INGESTION_COLLECTION_NAME = "sensor"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "future_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2