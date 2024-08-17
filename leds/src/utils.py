import pandas as pd
import os

def generateFile(stream: str) -> None:

  PROJECT_DIRPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

  if not os.path.exists(os.path.join(PROJECT_DIRPATH, "files")):

    os.mkdir(os.path.join(PROJECT_DIRPATH, "files"))

  file_stream = open(os.path.join(PROJECT_DIRPATH, "files", "results-info.txt"), 'a', encoding="utf-8")

  file_stream.write(stream)

  file_stream.close()

def generateTable(df: pd.DataFrame) -> None:

  PROJECT_DIRPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

  if not os.path.exists(os.path.join(PROJECT_DIRPATH, "files")):

    os.mkdir(os.path.join(PROJECT_DIRPATH, "files"))

  df.to_excel(os.path.join(PROJECT_DIRPATH, "files", "results.xlsx"))