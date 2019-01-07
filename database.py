import os
import json
from typing import List


class Database(object):
    def __init__(self, file_path: str = "db.json"):
        self._file_path = file_path
        self._ensure_initialization()
        self._data = self._load_data()

    def _ensure_initialization(self):
        exists = os.path.isfile(self._file_path)
        if not exists:
            with open(self._file_path, "w") as f:
                json.dump({"data": []}, f)

    def _load_data(self):
        with open(self._file_path) as f:
            data = json.load(f)

        return data

    def _save_data(self):
        with open(self._file_path, "w") as f:
            json.dump(self._data, f)

    def insert(self, object: object):
        if not object["_key"]:
            raise ValueError("Object in database has to have `_key` attribute")

        self._data["data"].append(object)

    def get(self, key: str) -> object:
        for obj in self._data["data"]:
            if obj["_key"] == key:
                return object

        return None

    def list_keys(self) -> List[str]:
        keys = []
        for obj in self._data["data"]:
            keys.append(obj["_key"])

        return keys

    def contains(self, key: str) -> bool:
        keys = self.list_keys()
        contains = key in keys

        return contains
