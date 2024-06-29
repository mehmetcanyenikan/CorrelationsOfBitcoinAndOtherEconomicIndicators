import pandas as pd


class data_read:
    def __init__(self, file_path, file_name):
        self._file_path = file_path
        self._file_name = file_name

    @property
    def file_path(self):
        return self._file_path

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, new_file_name):
        self._file_name = new_file_name

    @property
    def read_csv(self):
        other_csv = pd.read_csv(self.file_path + self.file_name)
        return other_csv
