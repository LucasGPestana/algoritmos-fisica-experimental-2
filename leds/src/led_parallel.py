from typing import List, Dict
import json

import pandas as pd

class ledParallel:

  def __init__(self) -> None:

    # Pegando os dados esperados

    expected_results = ledParallel.getResults("expected_values.json")

    df_expected_results = ledParallel.getStructuredData(expected_results)

    df_expected_results["value_interval"] = df_expected_results["value_interval"].str.split(" - ")

    df_expected_results["min_value"] = df_expected_results["value_interval"].apply(lambda x: x[0])
    df_expected_results["max_value"] = df_expected_results["value_interval"].apply(lambda x: x[1])

    df_expected_results["min_value"] = df_expected_results["min_value"].astype(float)
    df_expected_results["max_value"] = df_expected_results["max_value"].astype(float)

    df_expected_results = df_expected_results.drop("value_interval", axis=1)

    self.expected_results = df_expected_results
    
    # Pegando os dados obtidos

    obtained_results = ledParallel.getResults("obtained_values.json")

    df_obtained_results = ledParallel.getStructuredData(obtained_results)

    self.obtained_results = df_obtained_results

    self.__all_data = pd.merge(self.obtained_results, self.expected_results, "right", "color")
  
  @property
  def all_data(self):

    return self.__all_data
  
  @staticmethod
  def getResults(filename: str) -> pd.DataFrame:

    file_stream = open(filename, "rb")

    content = json.loads(file_stream.read())

    file_stream.close()

    df_expected_results = pd.DataFrame(content)

    return df_expected_results
  
  @staticmethod
  def getStructuredData(data: Dict[str, List[str | float]]) -> pd.DataFrame:

    return pd.DataFrame(data)
  
  # Verifica se os dados obtidos estão dentro do intervalo esperado
  def compareData(self) -> None:

    self.__all_data["valid"] = (self.all_data["value (V)"] >= self.all_data["min_value"]) & (self.all_data["value (V)"] <= self.all_data["max_value"])

