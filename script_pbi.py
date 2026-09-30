import pandas as pd
import sqlite3

conn = sqlite3.connect(r'C:\Users\gusta\Desktop\projeto3\v1\datasus.db')

df = pd.read_sql("SELECT * FROM prod_amb_sus", conn)

total_geral_df = pd.read_sql("SELECT * FROM total_geral", conn)