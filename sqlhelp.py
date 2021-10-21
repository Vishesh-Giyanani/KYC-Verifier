import mysql.connector
class SQLinitialize:
    def __init__(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            # TODO: MAKE SURE TO CHECK PASSWORD
            password='Nilay0309',
            database="KYC_Verifier",
        )
        
    def loadDetails(self,name,email,contact,dob,residense,pin,state,gender):
        try:
            print('Loading')
            self.name = name
            self.email = email
            self.contact = contact
            self.dob = dob
            self.residense = residense
            self.pin = pin
            self.state = state
            self.gender = gender
            self.mycursor=self.mydb.cursor()
            query="INSERT INTO kyc (name,email,contact,dob,residence,pin,state,gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            values=(f"{self.name}",f"{self.email}",f"{self.contact}",f"{self.dob}",f"{self.residense}",f"{self.pin}",f"{self.state}",f"{self.gender}")
            print(query,values)
            self.mycursor.execute(query,values)
            print('Executed')
            self.mydb.commit()
            print('Committed')
            return True
        except Exception as e:
            return (f"Register:{e}")

    def read(self,name):
        try:
            self.mycursor=self.mydb.cursor()
            self.mycursor.execute(f"SELECT * FROM kyc WHERE name='{name}'")
            self.myresult=self.mycursor.fetchall()
            if not self.myresult:
                print('Empty list')
                return False
            else:
                return self.myresult[0]
        except Exception as e:
            return (f"Read:{e}")
    
    def update(self,name,password,username):
        try:
            print(type(password))
            print(type(username))
            print(type(name))
            self.mycursor=self.mydb.cursor()
            self.mycursor.execute(f"UPDATE kyc SET password='{password}' WHERE name='{name}'")
            self.mycursor.execute(f"UPDATE kyc SET username ='{username}' WHERE name='{name}'")
            self.mydb.commit()
            return True
        except Exception as e:
            return e

if __name__=='__main__':
    sql=SQLinitialize()
    print(sql.update('Nilay Nitish Gaitonde','pass123','NilayG'))