import pyodbc

SERVER = 'DESKTOP-P7AP7U4'
DATABASE = 'IndustriasQueen'
USERNAME = 'sa'
PASSWORD = 'testesbancos123'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes;'

conn = pyodbc.connect(connectionString)

cursor = conn.cursor()