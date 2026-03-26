import pymysql
conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user= 'root',
    password = 'Root',
    database= '10k'
)
# print(conn)

cur = conn.cursor()
# cur.execute("Show tables")
# for i in cur:
#     print(i)
conn.commit()

class admin:
    # def __init__(self):
    #         self.name = input("Enter Name:")
    #         self.email = input("Enter Email:")
    #         self.password = input("Enter Password:")
    #         self.phone = int(input("Enter Phone Number:"))
    def insert(self):
        self.name = input("Enter Name:")
        self.email = input("Enter Email:")
        self.password = input("Enter Password:")
        self.phone = int(input("Enter Phone Number:"))
        ins = "insert into admin(name,email,password,phone) values (%s,%s,%s,%s)"
        cur.execute(ins,(self.name,self.email,self.password,self.phone))
        conn.commit()
        print("Successfully Admin is added")
    def update(self):
        column_name  = input("ENter Column Name to update:")
        new_data = input(f"ENter {column_name} to Update:")
        cond = input("Enter Condition Column_name:")
        cond_data = input("Enter Condition data:")
        a = '%s'
        q = f'update admin set {column_name} = {a} where {cond} = {a}'
        cur.execute(q,(new_data,cond_data))
        conn.commit()
        print("Succesfully Admin Details Updated")
    def delete(self):
        cond_column = input("Enter Condition Column Name:")
        cond_data = input("Enter Condition Data:")
        q = f'delete from admin where {cond_column} = {cond_data}'
        cur.execute(q)
        conn.commit()
        print("Succesfully Admin Details is deleted")
class trainer(admin):
    def insert(self):
        self.name = input("Enter Name:")
        self.email = input("Enter Email:")
        self.password = input("Enter Password:")
        self.phone = int(input("Enter Phone Number:"))
        ins = "insert into trainer(name,email,password,phone) values (%s,%s,%s,%s)"
        cur.execute(ins,(self.name,self.email,self.password,self.phone))
        conn.commit()
        print("Successfully Trainer is added")
    def update(self):
        column_name  = input("ENter Column Name to update:")
        new_data = input(f"ENter {column_name} to Update:")
        cond = input("Enter Condition Column_name:")
        cond_data = input("Enter Condition data:")
        a = '%s'
        q = f'update trainer set {column_name} = {a} where {cond} = {a}'
        cur.execute(q,(new_data,cond_data))
        conn.commit()
        print("Succesfully Trainer Details Updated")
    def delete(self):
        cond_column = input("Enter Condition Column Name:")
        cond_data = input("Enter Condition Data:")
        q = f'delete from trainer where {cond_column} = {cond_data}'
        cur.execute(q)
        conn.commit()
        print("Succesfully Trainer Details is deleted")
class pm(admin):
    def insert(self):
        self.name = input("Enter Name:")
        self.email = input("Enter Email:")
        self.password = input("Enter Password:")
        self.phone = int(input("Enter Phone Number:"))
        ins = "insert into pm(name,email,password,phone) values (%s,%s,%s,%s)"
        cur.execute(ins,(self.name,self.email,self.password,self.phone))
        conn.commit()
        print("Successfully PM is added")
    def update(self):
        column_name  = input("ENter Column Name to update:")
        new_data = input(f"ENter {column_name} to Update:")
        cond = input("Enter Condition Column_name:")
        cond_data = input("Enter Condition data:")
        a = '%s'
        q = f'update pm set {column_name} = {a} where {cond} = {a}'
        cur.execute(q,(new_data,cond_data))
        conn.commit()
        print("Succesfully PM Details Updated")
    def delete(self):
        cond_column = input("Enter Condition Column Name:")
        cond_data = input("Enter Condition Data:")
        q = f'delete from pm where {cond_column} = {cond_data}'
        cur.execute(q)
        conn.commit()
        print("Succesfully PM Details is deleted")
class student:
    # def __init__(self):
    #     self.name = input("Enter Name:")
    #     self.email = input("Enter Email:")
    #     self.password = input("Enter Password:")
    #     self.course = input("Enter Course:")
    #     self.branch = input("Enter Branch:")
    #     self.passout_year = input("Enter PassOut Year:")
    #     self.phone = int(input("Enter Phone Number:"))
    def insert(self):
        self.name = input("Enter Name:")
        self.email = input("Enter Email:")
        self.password = input("Enter Password:")
        self.course = input("Enter Course:")
        self.branch = input("Enter Branch:")
        self.passout_year = input("Enter PassOut Year:")
        self.phone = int(input("Enter Phone Number:"))
        ins = "insert into student(name,email,password,course,branch,passout_year,phone) values (%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(ins,(self.name,self.email,self.password,self.course,self.branch,self.passout_year,self.phone))
        conn.commit()
        print("Successfully Student is added")
    def update(self):
        column_name  = input("ENter Column Name to update:")
        new_data = input(f"ENter {column_name} to Update:")
        cond = input("Enter Condition Column_name:")
        cond_data = input("Enter Condition data:")
        a = '%s'
        q = f'update student set {column_name} = {a} where {cond} = {a}'
        cur.execute(q,(new_data,cond_data))
        conn.commit()
        print("Succesfully Student Details Updated")
    def delete(self):
        cond_column = input("Enter Condition Column Name:")
        cond_data = input("Enter Condition Data:")
        q = f'delete from student where {cond_column} = {cond_data}'
        cur.execute(q)
        conn.commit()
        print("Succesfully Student Details is deleted")
# a = student()
# a.insert()
while True:
    print("=========================================")
    print("              10000 Coders               ")
    print("=========================================")
    print("1.Admin\n2.Trainer\n3.PM\n4.Student\n5.Exit")
    try:
        op = int(input("Choose who are you: "))
        if op == 1:
            print("================================")
            print("    welcome to admin portal     ")
            print("================================")
            email = input("Enter email:")
            password = input("Enter Password: ")
            cur.execute("select * from admin")
            for i in cur:
                if email == i[2] and password == i[3]:
                    while True:
                        print("1.Admin\n2.Trainer\n3.PM\n4.Student\n5.Exit")
                        print("Choose your option:")
                        op = int(input("Enter Choosen Portal Option:"))
                        if op == 1:
                            print("1.Insert\n2.Update\n3.Delete")
                            p = int(input("Choose action:"))
                            if p == 1:
                                ad = admin()
                                ad.insert()
                            elif p == 2:
                                ad = admin()
                                ad.update()
                            else:
                                ad = admin()
                                ad.delete()
                        elif op == 2:
                            print("1.Insert\n2.Update\n3.Delete")
                            p = int(input("Choose action:"))
                            if p == 1:
                                ad = trainer()
                                ad.insert()
                            elif p == 2:
                                ad = trainer()
                                ad.update()
                            else:
                                ad = trainer()
                                ad.delete()
                        elif op == 3:
                            print("1.Insert\n2.Update\n3.Delete")
                            p = int(input("Choose action:"))
                            if p == 1:
                                ad = pm()
                                ad.insert()
                            elif p == 2:
                                ad = pm()
                                ad.update()
                            else:
                                ad = pm()
                                ad.delete()
                        elif op == 4:
                            print("1.Insert\n2.Update\n3.Delete")
                            p = int(input("Choose action:"))
                            if p == 1:
                                ad = student()
                                ad.insert()
                            elif p == 2:
                                ad = student()
                                ad.update()
                            else:
                                ad = student()
                                ad.delete()
                        elif op == 5:
                            break
                        else:
                            print("Choose correct Option")
                else:
                    print("Invalid Admin Credentials")
                conn.commit()
        elif op == 2:
            print("================================")
            print("    welcome to Trainer portal     ")
            print("================================")
            email = input("Enter email:")
            password = input("Enter Password: ")
            cur.execute("select * from trainer")
            for i in cur:
                if email == i[2] and password == i[3]:
                    while True:
                        print("1.PM\n2.Student\n3.Home\n4.Exit")
                        print("Choose your option:")
                        op = int(input("Enter Choosen Option:"))
                        if op == 1:
                            print("1.Insert\n2.Update\n3.Delete")
                            p = int(input("Choose action:"))
                            if p == 1:
                                ad = pm()
                                ad.insert()
                            elif p == 2:
                                ad = pm()
                                ad.update()
                            else:
                                ad = pm()
                                ad.delete()
                        elif op == 2:
                            print("1.Insert\n2.Update\n3.Delete")
                            p = int(input("Choose action:"))
                            if p == 1:
                                ad = student()
                                ad.insert()
                            elif p == 2:
                                ad = student()
                                ad.update()
                            else:
                                ad = student()
                                ad.delete()
                        elif op == 3:
                            print("Hi Trainer")
                        elif op == 4:
                            break
                        else:
                            print("Choose correct Option")
                else: 
                    print("Invalid Credentials")
            conn.commit()
        elif op == 3:
            print("================================")
            print("    welcome to PM portal     ")
            print("================================")
            email = input("Enter email:")
            password = input("Enter Password: ")
            cur.execute("select * from pm")
            for i in cur:
                if email == i[2] and password == i[3]:
                    while True:
                        print("1.Home\n2.Student\n3.Exit")
                        print("Choose your option:")
                        op = int(input("Enter Choosen Option:"))
                        if op == 1:
                            print("HI PM")
                        elif op == 2:
                            print("1.Insert\n2.Update\n3.Delete")
                            p = int(input("Choose action:"))
                            if p == 1:
                                ad = student()
                                ad.insert()
                            elif p == 2:
                                ad = student()
                                ad.update()
                            else:
                                ad = student()
                                ad.delete()
                        elif op == 3:
                            break
                        else:
                            print("Choose correct Option")
                else: 
                    print("Invalid Credentials")
            conn.commit()
        elif op == 4:
            print("================================")
            print("    welcome to Student portal     ")
            print("================================")
            email = input("Enter email:")
            password = input("Enter Password: ")
            cur.execute("select * from student")
            for i in cur:
                if email == i[2] and password == i[3]:
                    print("Hi Student")
                else: 
                    print("Invalid Credentials")
            conn.commit()
        elif op == 5:
            break
        else:
            print("Choose Correct options to login")
    except Exception as e:
        print(e)