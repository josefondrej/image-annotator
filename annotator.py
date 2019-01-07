from database import Database
from typing import List
import os


class Annotator(object):
    def __init__(self, image_directory: str = "./static/images", database_path: str = "db.json"):
        self._image_directory = image_directory
        self._database = Database(database_path)
        self._to_annotate = [img for img in self._list_all_images() if img not in self._list_annotated_images()]

    def _list_all_images(self) -> List[str]:
        image_names = os.listdir(self._image_directory)
        return image_names

    def _list_annotated_images(self):
        annotated_images = self._database.list_keys()
        return annotated_images

    def _db_format(self, image: str, xy: List[int]):
        db_entry = {"_key": image, "xy": xy}
        return db_entry

    def annotate(self, image: str, xy: List[int]):
        if self._database.contains(image):
            pass  # TODO: remove and then insert again

        db_entry = self._db_format(image, xy)
        self._database.insert(db_entry)
        self._to_annotate.remove(image)

    def next_to_annotate(self, full_path=True):
        if full_path:
            prefix = self._image_directory + "/"
        else:
            prefix = ""

        if self._to_annotate:
            return prefix + self._to_annotate[0]
        else:
            self._database._save_data()
            return None
