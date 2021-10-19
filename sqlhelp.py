import mysql.connector
class SQLinitialize:
    def __init__(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            # TODO: MAKE SURE TO CHECK PASSWORD
            password='',
            database="KYC_Verifier",
        )
        
    def register(self,name,email,contact,dob,residense,pin,state,gender):
        try:
            self.name = name
            self.email = email
            self.contact = contact
            self.dob = dob
            self.residense = residense
            self.pin = pin
            self.state = state
            self.gender = gender
            self.mycursor=self.mydb.cursor()
            query="INSERT INTO kyc (name,email,contact,dob,pin,state,gender) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values=(f"{self.name}",f"{self.email}",f"{self.contact}",f"{self.dob}",f"{self.pin}",f"{self.state}",f"{self.gender}")
            self.mycursor.execute(query,values)
            self.mydb.commit()
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

if __name__=='__main__':
    sql=SQLinitialize()
    print(sql.read('Nilay Gaitonde'))