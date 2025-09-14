from db import create_connection

#add
def add_student(std_name,std_age,gender,phone):
    conn = create_connection()
    cursor = conn.cursor()
    query="""insert into students(std_name,std_age,gender,phone)
         values(%s,%s,%s,%s)"""
    val=(std_name,std_age,gender,phone)
    cursor.execute(query,val)
    conn.commit()
    cursor.close()
    conn.close()

 #view
def view_student():
    conn=create_connection()
    cursor=conn.cursor()
    query="select * from students"
    cursor.execute(query)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    for row in result:
        print(row)
    return result

#update
def update_student(std_id,std_name,std_age,gender,phone):
    conn=create_connection()
    cursor=conn.cursor()
    update=[]
    values=[]
    if std_name:
        update.append("std_name=%s")
        values.append(std_name)
    if std_age:
        update.append("std_age=%s")
        values.append(std_age)
    if gender:
        update.append("gender=%s")
        values.append(gender)
    if phone:
        update.append("phone=%s")
        values.append(phone)
    if update:
        query=f"update students set {','.join(update)} where std_id=%s"
        values.append(std_id)                
        cursor.execute(query,tuple(values))
        conn.commit()
    cursor.close()
    conn.close()
#delete
def delete_student(std_id):
    conn=create_connection()
    cursor=conn.cursor()
    query="delete from students where std_id=%s"
    cursor.execute(query,(std_id,))
    conn.commit()
    cursor.close()      
    conn.close()

def search_student(keyword):
    conn=create_connection()
    cursor=conn.cursor()  
    query="select * from students where std_name like %s or phone like %s"
    cursor.execute(query,(f"%{keyword}%",f"%{keyword}%"))
    result=cursor.fetchall()
    for res in result:
        print(res)
    else:
        print("No matching records found.")
    cursor.close()
    conn.close()