from dataclasses import dataclass
from carl import libreoffice

@dataclass
class Model:
    path: str

    def load(self):
        libreoffice.connect_socket()
        self.doc = libreoffice.open_doc(self.path)

    def close(self):
        libreoffice.close_socket()

    def evaluate(self):
        pass

    def set_sheet_value(self, sheet_name: str, range_a1: str, value):
        sheet = libreoffice.get_sheet_by_name(self.doc, sheet_name)
        libreoffice.set_sheet_value(sheet, range_a1, value)

    def get_sheet_values(self, sheet_name: str, range_a1: str):
        sheet = libreoffice.get_sheet_by_name(self.doc, sheet_name)
        return libreoffice.get_sheet_values(sheet, range_a1)
