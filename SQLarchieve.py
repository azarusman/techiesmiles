import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

engine = create_engine('postgresql://postgres:NEWworld123@localhost:5432')
timestamp = datetime.now().strftime("%Y%m%d")

def call_dbengine(User_select_Query):
    try:
        sql_data = pd.read_sql(User_select_Query, engine)
        sql_data['salary'] = sql_data['salary']*2
        filename = f'Result_{timestamp}.csv'
        sql_data.to_csv(filename)
        print(f'Data extracted and saved to {filename}')
    except Exception as e:
        print(f"Error reading from the database: {e}")

def update_records(User_update_Query):
    try:
        with engine.connect() as connection:
            connection.execute(User_update_Query)
            connection.commit()
            print('Details are updated in the database')
    except Exception as e:
        print(f"Error updating records in the database: {e}")

if __name__ == "__main__":
    User_input = input(str('Do you need to Extract or Update? :')) # extract, Extract, EXTRACT, EXtract

    # Call functions based on user input
    if User_input.lower() == 'extract':
        # SELECT Process Parameters
        Select_table_name = input('Enter the table name: ')
        User_select_Query = text(f'SELECT * FROM {Select_table_name}')
        call_dbengine(User_select_Query)

    elif User_input.lower() == 'update':
        # UPDATE Process Parameters
        Update_table_name = input('Enter the table name: ')
        Update_field_name = input('Enter the field to be updated: ')
        Updated_value = input('Enter New value: ')
        Existing_value = input('Enter Previous value: ')
        User_update_Query = text(f'UPDATE {Update_table_name} SET {Update_field_name} = {Updated_value} WHERE {Update_field_name} IN ({Existing_value})')
        update_records(User_update_Query)
    else:
        print('Invalid input. Please enter either "Update" or "Extract".')




