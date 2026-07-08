import psycopg2

# ***********************************************************

def createtable_customer():
 
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
            
            # 2. สร้าง cursor
        cur = conn.cursor()

        # 3. กำหนดคำสั่ง SQL
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customer (
            cid serial primary key not null ,
            customername text ,
            taxid  text  ,
            address text  ,
            phone  text,
            status text
        );
        """


        # 4. ทำการ execute คำสั่ง
        cur.execute(create_table_query)

        # 5. Commit เพื่อบันทึกการเปลี่ยนแปลง
        conn.commit()
        print("สร้างตารางเรียบร้อยแล้ว")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
        # 6. ปิดการเชื่อมต่อ
        if cur:
            cur.close()
        if conn:
            conn.close()
    
        return "end"

# ************************************************************
