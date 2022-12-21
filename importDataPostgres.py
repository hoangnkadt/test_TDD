import sql_model #create table in database
import pandas as pd
from sqlalchemy import create_engine

# link to connet to database
engine = create_engine('postgresql://postgres:123@localhost/TDD-test')
# file input 
df=pd.read_csv('input.csv')
# import data in table
df.to_sql(name='PermutatedLeadStatusHistory',con=engine,if_exists='replace',index=False)