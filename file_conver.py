import pandas as pd

read_file = pd.read_excel (r'D:\Avid Data Science Services\AMTPL_Insurance\Actuary\Data\PData.xlsx')
read_file.to_csv (r'D:\Avid Data Science Services\AMTPL_Insurance\Actuary\Data\PData.csv', index = None, header=True)
