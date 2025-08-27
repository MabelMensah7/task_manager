from pymongo import MongoClient
import os

from dotenv import load_dotenv

load_dotenv()

# connect to mongo altas cluster
mongo_client = MongoClient(os.getenv("MONGO_URI"))

#access the data base
task_manager_db = mongo_client["task_manager_db"]

#pick a collection to operate on
tasks = task_manager_db["tasks"]

