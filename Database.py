import mysql.connector


class Database(object):
    myDatabase = None
    my_cursor = None

    def __init__(self):
        self.myDatabase = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd='root',
            database="eli_db2"
        )
        self.my_cursor = self.myDatabase.cursor()

    def add_user(self, user_id, name):
        self.my_cursor.execute("SELECT chat_id from users")      
        all_id = self.my_cursor.fetchall() ## it returns a list of all databases present
        chk = False
        for x  in all_id:
            if x[0]== user_id:
                print("user exist")
                chk=True
                break;
        if chk==False:
            
            sql = "insert into users (chat_id, name) VALUES (%s, %s)"
            val = (user_id, name)
            self.my_cursor.execute(sql, val)
            self.myDatabase.commit()
            print("user registered")
     

    def select_user(self):
        self.my_cursor.execute("SELECT chat_id from users")

        all_id = self.my_cursor.fetchall()

        whole_id=[]

        for x  in all_id:
            whole_id.append(x[0])
        return whole_id
        
    def select_name(self):
        self.my_cursor.execute("SELECT * from users")

        all_id = self.my_cursor.fetchall()

        whole_id=[]

        for x  in all_id:
            whole_id.append(x[1])
        return whole_id   
        
        
        
        
        