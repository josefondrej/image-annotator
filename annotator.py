from database import Database
from typing import List
import os


class Annotator(object):
    def __init__(self, picture_directory: str = "./static/pictures", database_path: str = "db.json"):
        self._picture_directory = picture_directory
        self._database = Database(database_path)
        self._to_annotate = [pic for pic in self._list_all_pictures() if pic not in self._list_annotated_pictures()]

    def _list_all_pictures(self) -> List[str]:
        picture_names = os.listdir(self._picture_directory)
        return picture_names

    def _list_annotated_pictures(self):
        annotated_pictures = self._database.list_keys()
        return annotated_pictures

    def _db_format(self, picture: str, xy: List[int]):
        db_entry = {"_key": picture, "xy": xy}
        return db_entry

    def annotate(self, xy: List[int]):
        picture = self.next_to_annotate(False)
        db_entry = self._db_format(picture, xy)
        self._database.insert(db_entry)
        print(picture)
        self._to_annotate.remove(picture)

    def next_to_annotate(self, full_path = True):
        if full_path:
            prefix = self._picture_directory + "/"
        else:
            prefix = ""

        if self._to_annotate:
            return prefix + self._to_annotate[0]
        else:
            self._database._save_data()
            return None


