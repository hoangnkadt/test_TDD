import os
import pandas as pd
from sqlalchemy import create_engine

def importData(tableInput,tableOutput):
  # link to connect to database
  engine = create_engine('postgresql://postgres:123@localhost/TDD-test')

  # Update file path to the correct location
  file_path = os.path.join(os.getcwd(), 'input', tableInput)

  # read the file
  df = pd.read_csv(file_path)

  # import data in table
  df.to_sql(name= tableOutput ,con=engine,if_exists='replace',index=False)