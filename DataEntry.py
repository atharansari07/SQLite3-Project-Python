class Student:
    def __init__(self) :
        self.Dict={}
    def MakingData(self):
        outer_dict=int(input("How many data you want to Enter :- "))
        for i in range(outer_dict):
            Name=input("\t\tEnter the Name :- ")
            inner_dict={}
            inner_size=int(input("Enter the Size for Inner Data's :- "))
            for j in range(inner_size):
                key=input("\t\t\tEnter the Key :- ")
                value=input("\t\t\tEnter the Value :- ")
                inner_dict[key]=value
            self.Dict[Name] = inner_dict    
    def Display_data(self):
        for outer_key,inner_dict in self.Dict.items():
            print(f"\n{outer_key}    :")
            for inner_key,value in inner_dict.items():
                print(f"\t\t {inner_key}    :   {value}")
    def Search_Data(self):
        name=input("Enter the name who's data you want to Search :- ")
        for outer_key,inner_dict in self.Dict.items():
           if name==outer_key:
               print(f"{outer_key}  :   {inner_dict}")
           else:
               print("Name is not availaible ")
    def Delete_Data(self):
        name=input("Enter the name who's data you want to delete :- ")
        del self.Dict[name]
        print("Data Delete Successfully ")
    def Update(self):
        name=input("Enter the name who's data you want to update :- ")
        if name==self.Dict:
            key=input("Enter the Key of which you want to change :- ")
            newValue=input("Enter the New Value :- ")
            self.Dict[name][key]=newValue
            print("Update Successfull")
        else:
            print("Name not found ! ")
        

class Teacher:
    def __init__(self):
        self.Dict={}
    def MakingData(self):
        outer_dict=int(input("Enter the Size how Many Data You want to Enter :- "))
        for i in range(outer_dict):
            Name=input("Enter The Name :- ")
            inner_dict=int(input("Enter the size  for inner Data :- "))
            for j in range(inner_dict):
                key=input("Enter the Key :- ")
                value=eval(input("Enter the Value :- "))
                inner_dict[key]=value
            self.Dict[Name]=inner_dict
    def Display_data(self):
        for outer_key,inner_dict in self.Dict.items():
            print(f"{outer_key}")
            for inner_key,value in inner_dict.items():
                print(f"\t\t {inner_key}    :   {value}")
    def Search_Data(self):
        name=input("Enter the name who's data you want to Search :- ")
        for outer_key,inner_dict in self.Dict.items():
           if name==outer_key:
               print(f"{outer_key}  :   {inner_dict}")
           else:
               print("Name is not availaible ")
    def Delete_Data(self):
        name=input("Enter the name who's data you want to delete :- ")
        del self.Dict[name]
        print("Data Delete Successfully ")
    def Update(self):
        name=input("Enter the name who's data you want to update :- ")
        if name==self.Dict:
            key=input("Enter the Key of which you want to change :- ")
            newValue=input("Enter the New Value :- ")
            self.Dict[name][key]=newValue
            print("Update Successfull")
        else:
            print("Name not found ! ")
    

print('''\t\t\tWelcome for Data Entery for Teachers and Student's ''')
std=Student()
Teac=Teacher()
while True:
    print('''
                1.Student's Data 
                2.Teacher's Data
                3.Exit From the Programme ''')
    choice=int(input("Enter Your Choice :- "))
    if choice==1:
        while True:
            print('''
                1.Enter Data and Add Data
                2.Display Data
                3.Search Student 
                4.Delete Student
                5.Update Student 
                6.Exit ''')
            ch=int(input("Enter Your Choice :- "))
            if ch==1:
                std.MakingData()
            elif ch==2:
                std.Display_data()
            elif ch==3:
                std.Search_Data()
            elif ch==4:
                std.Delete_Data()
            elif ch==5:
                std.Update()
            else:
                break
                print("Thanks...")
    elif choice==2:
         while True:
            print('''
                1.Enter Data and Add Data
                2.Display Data  
                3.Search Teacher 
                4.Delete Teacher
                5.Update Teacher
                6.Exit ''')
            ch=int(input("Enter Your Choice :- "))
            if ch==1:
                Teac.MakingData()
            elif ch==2:
                Teac.Display_data()
            elif ch==3:
                std.Search_Data()
            elif Teac==4:
                Teac.Delete_Data()
            elif ch==4:
                Teac.Update()
            else:
                break
                print("Thanks...")
    else:
         print("Thanks for using this Programme ")
         break