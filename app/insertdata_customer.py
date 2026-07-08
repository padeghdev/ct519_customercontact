import psycopg2

# ***********************************************************

def insertdata_customer():

    customername =   "AAA
    taxid  = "0122222366632"
    address = "123  sukhumwit rd. 10110"
    phone  = "0885555555"
    status = '1'


    conn = dbconn()
    cursor = conn.cursor()
    
    sql_query = "INSERT INTO customer  ( customername, taxid , address ,phone ,status ) VALUES (%s , %s , %s , %s , %s  ) ; "

 
    cursor.execute(sql_query, ( customername, taxid , address ,phone ,status  ))
    
    conn.commit()  
    cursor.close()  
    conn.close()   
        
 
    return "Table Created 11 Successfully"