import psycopg2

# ***********************************************************

def createtable_contact():
 
    conn  = None
    cur  = None
    try:
        conn = psycopg2.connect(
                dbname="mydatabase",
                user="myuser",
                password="mypassword",
                host="dbpg",
                port="5432"
            )
            
 
        cur = conn.cursor()

 
        create_table_query = """
        CREATE TABLE IF NOT EXISTS contact (
            conid serial primary key NOT NULL,
            contactdetail text ,
            cid bigint ,
            status character ,
            submitdate text,
            submittime text
        );
        """


 
        cur.execute(create_table_query)

    
        conn.commit()
        print("สร้างตารางเรียบร้อยแล้ว")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
 
        if cur:
            cur.close()
        if conn:
            conn.close()
    
        return "end"

# ************************************************************
