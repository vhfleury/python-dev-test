import sqlite3
from sqlite3 import Error

def criando_conexao(path = "data/teste.db" ):
    """create a database connection to a SQLite database"""
    
    conn = None
    try:
        conn = sqlite3.connect(path)
        
    except Error as e:
        print(e)
            
    return conn

def criando_tabela():
    
    """criando tabela"""

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
    
    s = "CREATE TABLE adult ("
    
    for col in colunas:
        s = s + col + ", "
    s = s[:-2] + ")"
        
    mydb = criando_conexao()
    mycursor = mydb.cursor()
    mycursor.execute(s)
    mydb.commit()
    mycursor.close()
    
    print("tabela adult criada")    

if __name__ == '__main__':
    criando_conexao()
    criando_tabela()