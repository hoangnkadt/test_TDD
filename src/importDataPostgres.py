import os
import pandas as pd
from sqlalchemy import create_engine


def importData(config,nameLink,tableInput,tableOutput):
  link = f"postgresql://{config['mySQL']['user']}:{config['mySQL']['password']}@{config['mySQL']['host']}/{config['mySQL']['db_name']}"
  # link to connect to database
  engine = create_engine(link)

  # Update file path to the correct location
  file_path = os.path.join(os.getcwd(), 'input',nameLink,tableInput)
  # read the file
  df = pd.read_csv(file_path)

  # import data in table
  df.to_sql(name= tableOutput ,con=engine,if_exists='replace',index=False)