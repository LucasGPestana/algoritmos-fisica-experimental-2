from src.led_parallel import ledParallel
from src.utils import generateFile, generateTable

if __name__ == "__main__":

  led_parallel = ledParallel()

  led_parallel.compareData()

  generateTable(led_parallel.all_data)
  
  generateFile(f"Quantos valores de tensão são válidos? {led_parallel.all_data['valid'].sum()}\n")
  generateFile(f"Porcentagem: {(led_parallel.all_data['valid'].sum() / led_parallel.all_data['valid'].count()) * 100}%\n")