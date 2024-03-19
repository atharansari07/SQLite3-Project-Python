import sqlite3
conn=sqlite3.connect("db.db")
curson=conn.cursor()
def InsertData():
    try:
        
        Id=int(input("Enter the Id :- "))
        name=input("Enter the Name :- ")
        Class=input("Enter the Class :- ")
        E_mail=input("Enter the E-mail Id :- ")
        curson.execute("""
INSERT INTO student(st_id, st_Name, st_Class, st_Email)
VALUES (?,?,?,?)""",
(Id,name,Class,E_mail))  
                       
        conn.commit()
        print('data inserted successfully!')
    except Exception as e:
        print(e)
def DisplayData():
    try:
        data=conn.execute("SELECT * FROM student")
        print("STUDENT ID \tSTUDENT NAME \t STUDENT CLASS \t      STUDENT E-MAIL ")
        for n in data:
            print(f"   {n[0]}       \t{n[1]}\t\t\t{n[2]}\t\t{n[3]}")
    except Exception as e:
        print(e)
def SearchData():
    try:
        print("\t\t\t1.Search By Name ")
        print("\t\t\t2.Search By Id  ")
        print("\t\t\t3.Exit")
        ch=int(input("Enter your choice :- "))
        if ch==1:
            try:
                name=input("Enter the name you want to search :- ")
                data=conn.execute(f"SELECT * FROM student WHERE st_Name='"+name+"'")
                for n in data:
                    print(f"   {n[0]}       \t{n[1]}\t\t\t{n[2]}\t\t{n[3]}")
                conn.commit()
            except Exception as e:
                print(e)

        elif ch==2:
            try:
                id=input("Enter the name you want to search :- ")
                data=conn.execute(f"SELECT * FROM student WHERE st_id='"+id+"'")
                for n in data:
                    print(f"   {n[0]}       \t{n[1]}\t\t\t{n[2]}\t\t{n[3]}")
                conn.commit()
            except Exception as e:
                print(e)

        else:
            print("Thanks...")
    except Exception as e:
        print(e)
def DeleteData():
    try:
        print("\t\t\t1.Delete By Name ")
        print("\t\t\t2.Delete By id  ")
        print("\t\t\t3.Exit")
        ch=int(input("Enter your choice :- "))
        if ch==1:
            try:
                
                name=input("Enter the name you want to search :- ")
                data=conn.execute("SELECT * FROM student WHERE st_Name='"+name+"'")
                for n in data:
                    print(f"   {n[0]}       \t{n[1]}\t\t\t{n[2]}\t\t{n[3]}")
                DEL=input("Are you want to delete Data ?\n \t\t\t\tyes/no\n\t\t\t\t")
                if DEL=="yes":
                    conn.execute(f"DELETE FROM student WHERE st_Name='"+name+"'")
                    conn.commit()
                    print("\t\t\tData Deleted Sucessfully  ")
                else:
                    print("Thanks")
            except Exception as e:
                print(e)


        elif ch==2:
            try:
                
                id=input("Enter the id you want to delete  :- ")
                data=conn.execute("SELECT * FROM student WHERE st_id='"+id+"'")
                for n in data:
                    print(f"   {n[0]}       \t{n[1]}\t\t\t{n[2]}\t\t{n[3]}")
                DEL=input("Are you want to delete Data ?\n \t\t\t\tyes/no\n\t\t\t\t")
                if DEL=="yes":
                    conn.execute(f"DELETE FROM student WHERE st_id='"+id+"'")
                    conn.commit()
                    print("\t\t\tData Deleted Sucessfully  ")
                else:
                    print("Thanks")
            except Exception as e:
                print(e)

        else:
            print("Thanks...")
    except Exception as e:
        print(e)
def UpdateData():
    try:
        print("\t\t\t\tWelcome in Updation Process!")
        print("\t\t\t\t1.Update By Name ")
        print("\t\t\t\t2.Update By Id ")
        print("\t\t\t\t3.Exit ")
        choice=int(input("Select Your Option by Given Number's 1,2 and 3 "))
        if choice==1:
            try:
                name=input("Enter the Name you want to Update All Data :- ")
                data=conn.execute("SELECT * FROM student WHERE st_Name='"+name+"'")
                for i in data:
                    print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}")
                update=input("Are you want to Update This Data \n\t\t\t\t yes/no\n\t\t\t\t")
                if update=='yes':
                    id=input("Enter the new Id :- ")
                    Class=input("Enter the new Class :- ")
                    E_mail=input("Enter the New Email :- ")
                    conn.execute("UPDATE Student SET st_id=?,st_Email=?,st_Class=? WHERE st_Name=?",(id,E_mail,Class,name))
                    conn.commit()
                    print("Record Updated Sucessfully !")
                else:
                    print("Record Not found !!")
                    print("\t\t\tThanks")
            except Exception as e:
                print(e)
        elif choice==2:
            try:
                id=input("Enter the id you want to Update All Data :- ")
                data=conn.execute("SELECT * FROM student WHERE st_Name='"+id+"'")
                for i in data:
                    print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}")
                update=input("Are you want to Update This Data \n\t\t\t\t yes/no\n\t\t\t\t")
                if update=='yes':
                    name=input("Enter the new Name :- ")
                    Class=input("Enter the new Class :- ")
                    E_mail=input("Enter the New Email :- ")
                    conn.execute("UPDATE Student SET st_Name=?,st_Email=?,st_Class=? WHERE st_id=?",(name,E_mail,Class,id))
                    conn.commit()
                    print("Record Updated Sucessfully !")
                else:
                    print("Record Not found !!")
                    print("\t\t\tThanks")
            except Exception as e:
                print(e)
   
        else:
            print("Thanks...")
    except Exception as e:
        print(e)
def AcendingOrder():
    try:
        f=conn.execute("select * from student order by st_Name")
        print("\t\t\tRecord in Acending Order ")
        print("STUDENT ID \tSTUDENT NAME \t STUDENT CLASS \t      STUDENT E-MAIL ")
        for i in f:
            print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}")
    except Exception as e:
        print(e)
def DecendingOrder():
    try:
        f=conn.execute("select * from student order by st_Name DESC")
        print("\t\t\tRecord in Acending Order ")
        print("STUDENT ID \tSTUDENT NAME \t STUDENT CLASS \t      STUDENT E-MAIL ")
        for i in f:
            print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}")
    except Exception as e:
        print(e)
def StartingInLimit():
    try:
        strt=input("How many Data you want to see from starting of the Table :- ")
        f=conn.execute("select * from Student limit "+strt+"")
        print("STUDENT ID \tSTUDENT NAME \t STUDENT CLASS \t      STUDENT E-MAIL ")
        for i in f:
            print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}")
    except Exception as e:
        print(e)
def EndingInLimit():
    try:
        strt=input("How many Data you want to see from starting of the Table :- ")
        f=conn.execute("select * from Student order by Desc limit "+strt+"")
        print("STUDENT ID \tSTUDENT NAME \t STUDENT CLASS \t      STUDENT E-MAIL ")
        for i in f:
            print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}")
    except Exception as e:
        print(e)
def CheckBychoice():
    try:
        strt=input("Enter the Staring Number :- ")
        end=input("Enter the Ending Number :- ")
        f=conn.execute("select * from Student limit "+strt+" offset "+end+"")
        print("STUDENT ID \tSTUDENT NAME \t STUDENT CLASS \t      STUDENT E-MAIL ")
        for i in f:
            print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}")
    except Exception as e:
        print(e)
def main():
    while True:
        print("\n\n\n")
        print("\t\t\t\t WELCOME TO STUDENT DATA ")
        print("\t\t1.Insert Data")
        print("\t\t2.Display all Data")
        print("\t\t3.Search Data ")
        print("\t\t4.Delete Specific Data")
        print("\t\t5.Updata Data ")
        print("\t\t6.Check Record in Acending Order ")
        print("\t\t7.Check Record in Decending Order ")
        print("\t\t8.Check Data in Limit from the Starting of table ")
        print("\t\t9.Check Data in Limit from the Ending of table ")
        print("\t\t10.Check Data from your choice ")
        print("\t\t11.Exit")
        choice=int(input("Enter Your choice :- "))
        if choice==1:
            InsertData()
        elif choice==2:
            DisplayData()
        elif choice ==3:
            SearchData()
        elif choice==4:
            DeleteData()
        elif choice==5:
            UpdateData()
        elif choice==6:
            AcendingOrder()
        elif choice==7:
            DecendingOrder()
        elif choice==8:
            StartingInLimit()
        elif choice==9:
            EndingInLimit()
        elif choice==10:
            CheckBychoice()
        else:
            print("Thanks for using this programme !")
            break
main()
conn.close()