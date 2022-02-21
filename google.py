# import read_Hospital_Excel_Sheet
# import Write_Hospital_Excel_Sheet
 
# def AppointmentIndexInDoctorsDataBase (patient_ID) :
# for i in Doctors_DataBase :
# for j in Doctors_DataBase&#91;i] :
# if str(patient_ID) == str(j&#91;0]) :
# Appointment_index = Doctors_DataBase&#91;i].index(j)
# return Appointment_index,i
 
print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome Hospital Management System                     *")
print("*                                                                          *")
print("****************************************************************************")
tries = 0
tries_flag = ""
while tries_flag != "Close the program" :

    print("-----------------------------------------")
    print("|Enter 1 for Admin mode |\n|Enter 2 for user mode |")
    print("-----------------------------------------")
    Admin_user_mode = input("Enter your mode : ")
    
if Admin_user_mode == "1" : #Admin mode
    print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")
Password = input("Please enter your password : ")
while True :
    if Password == "1234" :
        print("-----------------------------------------")
print("|To manage patients Enter 1 |\n|To manage docotrs Enter 2 |\n|To manage appointments Enter 3 |\n|To be back Enter E |")
print("-----------------------------------------")
AdminOptions = input ("Enter your choice : ")
AdminOptions = AdminOptions.upper()
if AdminOptions == "1" : #Admin mode --&gt; Pateints Management
    print("-----------------------------------------")
    print("|To add new patient Enter 1    |")
    print("|To display patient Enter 2    |")
    print("|To delete patient data Enter 3 |")
    print("|To edit patient data Enter 4     |")
    print("|To Back enter B       |")
print("-----------------------------------------")
Admin_choice = input ("Enter your choice : ")
Admin_choice = Admin_choice.upper()
if Admin_choice == "1" : #Admin mode --&gt; Pateints Management --&gt; Enter new patient data
try : #To avoid non integer input
patient_ID = int(input("Enter patient ID : "))
while patient_ID in Pateints_DataBase : #if Admin entered used ID
patient_ID = int(input("This ID is unavailable, please try another ID : "))
Department=input("Enter patient department                : ")
DoctorName=input("Enter name of doctor following the case : ")
Name      =input("Enter patient name                      : ")
Age       =input("Enter patient age                       : ")
Gender    =input("Enter patient gender                    : ")
Address   =input("Enter patient address                   : ")
RoomNumber=input("Enter patient room number               : ")
Pateints_DataBase&#91;patient_ID]=&#91;Department,DoctorName,Name,Age,Gender,Address,RoomNumber]
print("----------------------Patient added successfully----------------------")
except :
print("Patient ID should be an integer number")
elif Admin_choice == "2" : #Admin mode --&gt; Pateints Management --&gt; Display patient data
try : #To avoid non integer input
patient_ID = int(input("Enter patient ID : "))
while patient_ID not in Pateints_DataBase :
patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
print("\npatient name        : ",Pateints_DataBase&#91;patient_ID]&#91;2])
print("patient age         : ",Pateints_DataBase&#91;patient_ID]&#91;3])
print("patient gender      : ",Pateints_DataBase&#91;patient_ID]&#91;4])
print("patient address     : ",Pateints_DataBase&#91;patient_ID]&#91;5])
print("patient room number : ",Pateints_DataBase&#91;patient_ID]&#91;6])
print("patient is in "+Pateints_DataBase&#91;patient_ID]&#91;0]+" department")
print("patient is followed by doctor : "+Pateints_DataBase&#91;patient_ID]&#91;1])
except :
print("Patient ID should be an integer number")
elif Admin_choice == "3" : #Admin mode --&gt; Pateints Management --&gt; Delete patient data
try : #To avoid non integer input
patient_ID = int(input("Enter patient ID : "))
while patient_ID not in Pateints_DataBase :
patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
Pateints_DataBase.pop(patient_ID)
print("----------------------Patient data deleted successfully----------------------")
except :
print("Patient ID should be an integer number")
elif Admin_choice == "4" : #Admin mode --&gt; Pateints Management --&gt; Edit patient data
try : #To avoid non integer input
patient_ID=int(input("Enter patient ID : "))
while patient_ID not in Pateints_DataBase :
patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
while True :
print("------------------------------------------")
print("|To Edit pateint Department Enter 1 :    |")
print("|To Edit Doctor following case Enter 2 : |")
print("|To Edit pateint Name Enter 3 :          |")
print("|To Edit pateint Age Enter 4 :           |")
print("|To Edit pateint Gender Enter 5 :        |")
print("|To Edit pateint Address Enter 6 :       |")
print("|To Edit pateint RoomNumber Enter 7 :    |")
print("|To be Back Enter B                      |")
print("-----------------------------------------")
Admin_choice = input("Enter your choice : ")
Admin_choice = Admin_choice.upper()
if Admin_choice == "1" :
Pateints_DataBase&#91;patient_ID]&#91;0]=input("\nEnter patient department : ")
print("----------------------Patient Department edited successfully----------------------")
elif Admin_choice == "2" :
Pateints_DataBase&#91;patient_ID]&#91;1]=input("\nEnter Doctor follouing case : ")
print("----------------------Doctor follouing case edited successfully----------------------")
elif Admin_choice == "3" :
Pateints_DataBase&#91;patient_ID]&#91;2]=input("\nEnter patient name : ")
print("----------------------Patient name edited successfully----------------------")
elif Admin_choice == "4" :
Pateints_DataBase&#91;patient_ID]&#91;3]=input("\nEnter patient Age : ")
print("----------------------Patient age edited successfully----------------------")
elif Admin_choice == "5" :
Pateints_DataBase&#91;patient_ID]&#91;4]=input("\nEnter patient gender : ")
print("----------------------Patient address gender successfully----------------------")
elif Admin_choice == "6" :
Pateints_DataBase&#91;patient_ID]&#91;5]=input("\nEnter patient address : ")
print("----------------------Patient address edited successfully----------------------")
elif Admin_choice == "7" :
Pateints_DataBase&#91;patient_ID]&#91;6]=input("\nEnter patient RoomNumber : ")
print("----------------------Patient RoomNumber edited successfully----------------------")
elif Admin_choice == "B" :
break
else :
print("Please Enter a correct choice")
except :
print("Patient ID should be an integer number")
elif Admin_choice == "B" : #Admin mode --&gt; Pateints Management --&gt; Back
break
else :
print("Please enter a correct choice\n")
elif AdminOptions == "2" : #Admin mode --&gt; Doctors Management
print("-----------------------------------------")
print("|To add new doctor Enter 1              |")
print("|To display doctor Enter 2              |")
print("|To delete doctor data Enter 3          |")
print("|To edit doctor data Enter 4            |")
print("|To be back enter B                     |")
print("-----------------------------------------")
Admin_choice = input ("Enter your choice : ")
Admin_choice = Admin_choice.upper()
if Admin_choice == "1" : #Admin mode --&gt; Doctors Management --&gt; Enter new doctor data
try : #To avoid non integer input
Doctor_ID = int(input("Enter doctor ID : "))
while Doctor_ID in Doctors_DataBase : #if Admin entered used ID
Doctor_ID = int(input("This ID is unavailable, please try another ID : "))
Department=input("Enter Doctor department : ")
Name      =input("Enter Doctor name       : ")
Address   =input("Enter Doctor address    : ")
Doctors_DataBase&#91;Doctor_ID]=&#91;&#91;Department,Name,Address]]
print("----------------------Doctor added successfully----------------------")
except :
print("Doctor ID should be an integer number")
elif Admin_choice == "2" : #Admin mode --&gt; Doctors Management --&gt; Display doctor data
try : #To avoid non integer input
Doctor_ID = int(input("Enter doctor ID : "))
while Doctor_ID not in Doctors_DataBase :
Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
print("Doctor name    : ",Doctors_DataBase&#91;Doctor_ID]&#91;0]&#91;1])
print("Doctor address : ",Doctors_DataBase&#91;Doctor_ID]&#91;0]&#91;2])
print("Doctor is in "+Doctors_DataBase&#91;Doctor_ID]&#91;0]&#91;0]+" department")
except :
print("Doctor ID should be an integer number")
elif Admin_choice == "3" : #Admin mode --&gt; Doctors Management --&gt; Delete doctor data
try : #To avoid non integer input
Doctor_ID = int(input("Enter doctor ID : "))
while Doctor_ID not in Doctors_DataBase :
Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
Doctors_DataBase.pop(Doctor_ID)
print("/----------------------Doctor data deleted successfully----------------------/")
except :
print("Doctor ID should be an integer number")
 
elif Admin_choice == "4" : #Admin mode --&gt; Doctors Management --&gt; Edit Doctor data
try : #To avoid non integer input
Doctor_ID=input("Enter doctor ID : ")
while Doctor_ID not in Doctors_DataBase :
Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
print("-----------------------------------------")
print("|To Edit doctor's department Enter 1    |")
print("|To Edit doctor's name Enter 2          |")
print("|To Edit doctor's address Enter 3       |")
print("To be Back Enter B                      |")
print("-----------------------------------------")
Admin_choice=input("Enter your choice : ")
Admin_choice = Admin_choice.upper()
if Admin_choice == "1" :
Doctors_DataBase&#91;Doctor_ID]&#91;0]&#91;0]=input("Enter Doctor's Department : ")
print("/----------------------Doctor's department edited successfully----------------------/")
elif Admin_choice == "2" :
Doctors_DataBase&#91;Doctor_ID]&#91;0]&#91;1]=input("Enter Doctor's Name : ")
print("----------------------Doctor's name edited successfully----------------------")
elif Admin_choice == "3" :
Doctors_DataBase&#91;Doctor_ID]&#91;0]&#91;2]=input("Enter Doctor's Address : ")
print("----------------------Doctor's address edited successfully----------------------")
elif Admin_choice == "B" :
break
else :
print("\nPlease enter a correct choice\n")
except :
print("Doctor ID should be an integer number")
elif Admin_choice == "B" : #Back
break
else :
print("\nPlease enter a correct choice\n")
elif AdminOptions == "3" : #Admin mode --&gt; Appointment Management
print("-----------------------------------------")
print("|To book an appointment Enter 1         |")
print("|To edit an appointment Enter 2         |")
print("|To cancel an appointment Enter 3       |")
print("|To be back enter B                     |")
print("-----------------------------------------")
Admin_choice = input ("Enter your choice : ")
Admin_choice = Admin_choice.upper()
if Admin_choice == "1" : #Admin mode --&gt; Appointment Management --&gt; Book an appointment
try : #To avoid non integer input
Doctor_ID = int(input("Enter the ID of doctor : "))
while Doctor_ID not in Doctors_DataBase :
Doctor_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID : "))
print("---------------------------------------------------------")
print("|For book an appointment for an exist patient Enter 1   |\n|For book an appointment for a new patient Enter 2      |\n|To be Back Enter B                                     |")
print("---------------------------------------------------------")
Admin_choice = input ("Enter your choice : ")
Admin_choice = Admin_choice.upper()
if Admin_choice == "1" :
patient_ID = int(input("Enter patient ID : "))
while patient_ID not in Pateints_DataBase : #if Admin entered incorrect ID
patient_ID = int(input("Incorrect ID, please Enter a correct patient ID : "))
elif Admin_choice == "2" :
patient_ID = int(input("Enter patient ID : "))
while patient_ID in Pateints_DataBase : #if Admin entered used ID
patient_ID = int(input("This ID is unavailable, please try another ID : "))
Department=Doctors_DataBase&#91;Doctor_ID]&#91;0]&#91;0]
DoctorName=Doctors_DataBase&#91;Doctor_ID]&#91;0]&#91;1]
Name      =input("Enter patient name    : ")
Age       =input("Enter patient age     : ")
Gender    =input("Enter patient gender  : ")
Address   =input("Enter patient address : ")
RoomNumber=""
Pateints_DataBase&#91;patient_ID]=&#91;Department,DoctorName,Name,Age,Gender,Address,RoomNumber]
elif Admin_choice == "B" :
break
Session_Start = input("Session starts at : ")
while Session_Start&#91; :2] == "11" or Session_Start&#91; :2] == "12" :
Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
for i in Doctors_DataBase&#91;Doctor_ID] :
if type(i&#91;0])!=str :
while Session_Start &gt;= i&#91;1] and Session_Start &lt; i&#91;2] :
Session_Start = input("This appointment is already booked, Please Enter an other time for start of session : ")
Session_End   = input("Session ends at : ")
New_Appointment=list()
New_Appointment.append(patient_ID)
New_Appointment.append(Session_Start)
New_Appointment.append(Session_End)
Doctors_DataBase&#91;Doctor_ID].append(New_Appointment)
print("/----------------------Appointment booked successfully----------------------/")
except :
print("Doctor ID should be an integer number")
elif Admin_choice == "2" : #Admin mode --&gt; Appointment Management --&gt; Edit an appointment
try : #To avoid non integer input
patient_ID = int(input("Enter patient ID : "))
while patient_ID not in Pateints_DataBase :
patient_ID = int(input("Incorrect Id, Please Enter correct patient ID : "))
try :   #To avoid no return function
AppointmentIndex,PairKey = AppointmentIndexInDoctorsDataBase(patient_ID)
Session_Start = input ("Please enter the new start time : ")
while Session_Start&#91; :2] == "11" or Session_Start&#91; :2] == "12" :
Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
for i in Doctors_DataBase&#91;Doctor_ID] :
if type(i&#91;0])!=str :
while Session_Start &gt;= i&#91;1] and Session_Start &lt; i&#91;2] :
Session_Start = input("This appointment is already booked, Please Enter an other time for start of session : ")
Session_End = input ("Please enter the new end time : ")
Doctors_DataBase&#91;PairKey]&#91;AppointmentIndex]=&#91;patient_ID,Session_Start,Session_End]
print("/----------------------appointment edited successfully----------------------/")
except :
print("No Appointment for this patient")
except :
print("Doctor ID should be an integer number")
elif Admin_choice == "3" : #Admin mode --&gt; Appointment Management --&gt; Cancel an appointment
try : #To avoid non integer input
patient_ID = int(input("Enter patient ID : "))
while patient_ID not in Pateints_DataBase :
patient_ID = int(input("Invorrect ID, Enter patient ID : "))
try :
AppointmentIndex,PairKey = AppointmentIndexInDoctorsDataBase(patient_ID)
Doctors_DataBase&#91;PairKey].pop(AppointmentIndex)
print("/----------------------appointment canceled successfully----------------------/")
except :
print("No Appointment for this patient")
except : #To avoid no return function
print("Patient ID should be an integer number")
elif Admin_choice == "B" : #Back
break
else :
print("please enter a correct choice")
elif AdminOptions == "B" : #Back
break
else :
print("Please enter a correct option")
elif Password != "1234" :
if tries &lt; 2 :
Password = input("Password incorrect, please try again : ")
tries += 1
else :
print("Incorrect password, no more tries")
tries_flag = "Close the program"
break
Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Pateints_DataBase)
Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)
elif Admin_user_mode == "2" : #User mode
print("****************************************\n|         Welcome to user mode         |\n****************************************")
while True :
print("\n-----------------------------------------")
print("|To view hospital's departments Enter 1 |")
print("|To view hospital's docotrs Enter 2     |")
print("|To view patients' residents Enter 3    |")
print("|To view patient's details Enter 4      |")
print("|To view doctor's appointments Enter 5  |")
print("|To be Back Enter B                     |")
print("-----------------------------------------")
UserOptions = input("Enter your choice : ")
UserOptions = UserOptions.upper()
if   UserOptions == "1" : #User mode --&gt; view hospital's departments
print("Hospital's departments :")
for i in Doctors_DataBase :
print(" "+Doctors_DataBase&#91;i]&#91;0]&#91;0])
elif UserOptions == "2" : #User mode --&gt; view hospital's Doctors
print("Hospital's doctors :")
for i in Doctors_DataBase :
print(" "+Doctors_DataBase&#91;i]&#91;0]&#91;1]+" in "+Doctors_DataBase&#91;i]&#91;0]&#91;0]+" department, from "+Doctors_DataBase&#91;i]&#91;0]&#91;2])
elif UserOptions == "3" : #User mode --&gt; view patients' residents
for i in Pateints_DataBase :
print(" Patient : "+Pateints_DataBase&#91;i]&#91;2]+" in "+Pateints_DataBase&#91;i]&#91;0]+" department and followed by "+Pateints_DataBase&#91;i]&#91;1]+", age : "+Pateints_DataBase&#91;i]&#91;3]+", from : "+Pateints_DataBase&#91;i]&#91;5]+", RoomNumber : "+Pateints_DataBase&#91;i]&#91;6])
elif UserOptions == "4" : #User mode --&gt; view patient's details
try : #To avoid non integer input
patient_ID = int(input("Enter patient's ID : "))
while patient_ID not in Pateints_DataBase :
patient_ID = int(input("Incorrect Id, Please enter patient ID : "))
print(" patient name        : ",Pateints_DataBase&#91;patient_ID]&#91;2])
print(" patient age         : ",Pateints_DataBase&#91;patient_ID]&#91;3])
print(" patient gender      : ",Pateints_DataBase&#91;patient_ID]&#91;4])
print(" patient address     : ",Pateints_DataBase&#91;patient_ID]&#91;5])
print(" patient room number : ",Pateints_DataBase&#91;patient_ID]&#91;6])
print(" patient is in "+Pateints_DataBase&#91;patient_ID]&#91;0]+" department")
print(" patient is followed by doctor : "+Pateints_DataBase&#91;patient_ID]&#91;1])
except :
print("Patient ID should be an integer number")
elif UserOptions == "5" : #User mode --&gt; view doctor's appointments
try : #To avoid non integer input
Doctor_ID = int(input("Enter doctor's ID : "))
while Doctor_ID not in Doctors_DataBase :
Doctor_ID = int(input("Incorrect Id, Please enter doctor ID : "))
print(Doctors_DataBase&#91;Doctor_ID]&#91;0]&#91;1]+" has appointments :")
for i in Doctors_DataBase&#91;Doctor_ID] :
if type(i&#91;0])==str :
continue
else :
print(" from : "+i&#91;1]+"    to : "+i&#91;2])
except :
print("Doctor ID should be an integer number")
elif UserOptions == "B" : #Back
break
else :
print("Please Enter a correct choice")
else :
print("Please choice just 1 or 2")