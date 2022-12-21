import sql_model
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:123@localhost/TDD-test')
df=pd.read_csv('input.csv')
df.to_sql(name='PermutatedLeadStatusHistory',con=engine,if_exists='replace',index=False)