import sqlite3
from sqlite3 import Error

# def criando_conexao(path =  ):
#     """create a database connection to a SQLite database"""
    
#     conn = None
#     try:
#         conn = sqlite3.connect(path)
        
#     except Error as e:
#         print(e)
            
#     return conn

def criando_tabela():
    """criando tabela adult"""

    colunas =   ["ID_adult integer PRIMARY KEY AUTOINCREMENT",
                'age TINYINT',
                'workclass VARCHAR(17)',
                'fnlwgt INT',
                'education VARCHAR(13)',
                'education_num TINYINT',
                'marital_status VARCHAR(22)',
                'occupation VARCHAR(18)',
                'relationship VARCHAR(15)',
                'race VARCHAR(19)',
                'sex VARCHAR(7)',
                'capital_gain MEDIUMINT',
                'capital_loss MEDIUMINT',
                'hours_per_week TINYINT',
                'native_country VARCHAR(27)',
                'class VARCHAR(7)']
    
    
    query = "CREATE TABLE adult("
    for col in colunas:
        query = query + col + ", "
    query = query[:-2] + ")"
        
    mydb = sqlite3.connect("data/adult.db")
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    
    print("tabela adult criada")    

if __name__ == '__main__':
    criando_tabela()