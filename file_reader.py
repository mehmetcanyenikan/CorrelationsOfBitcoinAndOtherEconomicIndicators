import os
import glob
from abc import ABC, abstractmethod

class ReadFolderFiles(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def read(self):
        pass

class ReadFolderCsvFiles(ReadFolderFiles):
    @property
    def read(self):
        csv_files = glob.glob(os.path.join(self.path, '*.csv'))
        csv_file_names = [os.path.basename(file) for file in csv_files]
        return csv_file_names
