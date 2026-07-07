import psycopg2

# ***********************************************************

def createtable():
 
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
        CREATE TABLE contact (
            conid bigint NOT NULL,
            contactdetail text ,
            cid bigint ,
            status character ,
            submitdate text,
            submittime text
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
