from dataclasses import dataclass
import pymongo
import os


@dataclass
class EnvironmentVariables:
    mongo_db_url = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariables()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)

