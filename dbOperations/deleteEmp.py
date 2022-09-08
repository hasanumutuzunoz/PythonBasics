import mysql.connector

def delete(id):
    conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Drakan9135')

    if conn.is_connected():
        print("Connected to mysql db")
        cursor = conn.cursor()

        # srt is our mysql query to delete the row id = '%d' from emp table
        str = "delete from emp where id = '%d'"
        args = (id)
        try:
            cursor.execute(str % args) #cursor.execute("delete from emp where id = '%d'" % id)
            conn.commit()
            print("Employee Deleted")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empId = int(input('Enter Emp Id:'))
delete(empId)
