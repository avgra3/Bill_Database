
import pandas as pd
from sqlalchemy import create_engine


# Getting the data for the database from an excel file
# This will make seperate variables from the different sheets on the excel file
path_to_excel = 'C:\\Users\\Gradillas\\Desktop\\tblBills.xlsx'

# Pandas dataframes for each table
carriers = pd.read_excel(path_to_excel,
                        sheet_name='carriers',
                        header=0)


products = pd.read_excel(path_to_excel,
                        sheet_name='products',
                        header=0)

bills = pd.read_excel(path_to_excel,
                        sheet_name='bills',
                        header=0)

billsPaid = pd.read_excel(path_to_excel,
                        sheet_name='billsPaid',
                        header=0)

# Getting the connection for the database
user = 'admin'
password = 'geeky'
host='localhost'
port=3306
database='billing'

# Creating connection to database
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# Inserting into the database
carriers.to_sql('bills_carriers', engine, if_exists='append', index=False)
products.to_sql('bills_products', engine, if_exists='append', index=False)
bills.to_sql('bills_bills', con=engine, if_exists='append', index=False)
billsPaid.to_sql('bills_billspaid', con=engine, if_exists='append', index=False)