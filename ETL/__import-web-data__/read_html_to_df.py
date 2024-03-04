# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:13:43 2023

@author: miros
"""


import pandas as pd

dfs = pd.read_html('https://www.w3schools.com/html/html_tables.asp')
for df in dfs:
    print(df)
    

file_name = r'C:\Users\miros\infoSec\Python_Infosec\PythonProgrammer\Useful_programs\dftable.xlsx'

with pd.ExcelWriter(file_name) as w:
    for i, df in enumerate(dfs):
        df.to_excel(w, sheet_name=f"sheet{i}",index=False)