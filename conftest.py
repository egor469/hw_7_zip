from zipfile import ZipFile
import pytest
import os.path
import shutil

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")


@pytest.fixture(scope="function", autouse=True)
def new_archive():
    if not os.path.exists(TMP_DIR):
        os.mkdir(TMP_DIR)
    with ZipFile("tmp_zip_test.zip", "w") as zip_file:
        for file in "CSV.csv", "PDF.pdf", "XLSX.xlsx":
            add_file = os.path.join(TMP_DIR, file)
            zip_file.write(add_file, os.path.basename(add_file))

    shutil.move("tmp_zip_test.zip", TMP_DIR)
    yield
    os.remove(TMP_DIR + "/tmp_zip_test.zip")
