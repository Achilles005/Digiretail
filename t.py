from urllib import parse
from sqlalchemy import create_engine
import pandas as pd
grp=pd.read_csv('g.csv')
prd=pd.read_csv('p.csv')

connecting_string = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:12sqlexpress.database.windows.net,1433;Database=Project;Uid=achilles;Pwd=RitaDinesh0506;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
params = parse.quote_plus(connecting_string)

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
#connection = engine.connect()
grp.to_sql('grp',con=engine ,if_exists = 'append', chunksize = 1000)
prd.to_sql('product',con=engine ,if_exists = 'append', chunksize = 1000)
print("Done")