import os
import sys
from dotenv import load_dotenv
from typing import Any

load_dotenv()

LIBREOFFICE_PATH = os.getenv("LIBREOFFICE_PATH", "/usr/lib/libreoffice")

sys.path.insert(0, f"{LIBREOFFICE_PATH}/program")

# To get working on my operating system (Arch)
os.environ["PATH"] = f"{os.environ['PATH']}:{LIBREOFFICE_PATH}/program"
os.environ["URE_BOOTSTRAP"] = f"vnd.sun.star.pathname:{LIBREOFFICE_PATH}/program/fundamentalrc"
os.environ["UNO_PATH"] = f"{LIBREOFFICE_PATH}/program"
os.environ["LD_LIBRARY_PATH"] = f"{LIBREOFFICE_PATH}/program:{LIBREOFFICE_PATH}/ure/lib"
os.environ["PYTHONPATH"] = f"{LIBREOFFICE_PATH}/program/:{os.environ.get('PYTHONPATH')}"

import uno

from ooodev.loader import Lo
from ooodev.calc import CalcDoc, CalcSheet

def connect_socket():
    Lo.load_office(Lo.ConnectSocket())

def open_doc(path: str) -> CalcDoc:
    return CalcDoc.open_doc(path, visible=False)

def close_socket():
    Lo.close_office()

def get_sheet_by_name(doc: CalcDoc, sheet_name: str) -> CalcSheet:
    return doc.sheets[sheet_name]

def get_sheet_value(sheet: CalcSheet, range_a1: str) -> Any:
    return sheet.get_val(cell_name=range_a1)

def get_sheet_values(sheet: CalcSheet, range_a1: str) -> Any:
    return sheet.get_array(range_name=range_a1)

def set_sheet_value(sheet: CalcSheet, range_a1: str, value):
    sheet.set_val(value=value, cell_name=range_a1)

if __name__=="__main__":
    connect_socket()
    doc = open_doc("test.ods")
    close_socket()

