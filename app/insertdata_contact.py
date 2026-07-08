import psycopg2

# ***********************************************************

def insertdata_customer():
    
    print ("Hello")
    cname =   "AAA
    address = "456  sukhumwit rd. 10110"


    # 2. คำสั่งสำหรับ PostgreSQL
    conn = dbconn()
    cursor = conn.cursor()
    
    sql_query = "INSERT INTO custom  ( cname , address ) VALUES (%s , %s  ) ; "

    # รันคำสั่ง SQL
    cursor.execute(sql_query, (cname , address))
    
    conn.commit()  # บันทึกข้อมูล
    cursor.close() # ปิด cursor
    conn.close()   # ปิดการเชื่อมต่อ
        
        # 3. รีไดเรกต์กลับไปหน้าแรก (Root)
    return "Table Created 11 Successfully"