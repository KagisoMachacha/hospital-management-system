

print("********************************************************************************************")
print("*                                                                                          *")
print("*                   Welcome To Louis Pasture Hospital Management System                    *")
print("*                                                                                          *")
print("********************************************************************************************\n")

# def sign_up():
#     global username_list
#     global password_list

#     print("please provide your credentials to access your account or create a new account.")
#     user = input("please enter 1 to create a new account or 2 for accessing your account: " )
#     if user == 2:
#         username = input("Username: ")
#         password = input("Password: ")

#         if username in username_list:
#             username_list.append(username)

#         elif password in password_list:
#             password_list.append(password)
#         print('You\'ve successfully been logged in.')

#     elif user == 1:
#         username = input("Username: ")
#         while True:
#             password = input("Password: ")
#             if len(password) <= 4:
#                 print("please enter a more stronger password")


def patient_details():
    while True:
        unique_id = input("please enter patient's unique code to retrieve their details: ")
        if unique_id == '1234':
            print("\n")
            print("Name and Surname of patient: Julia Pedro")
            print("Date Of Birth(yyyy/mm/dt): 1984 may 23")
            print("Age: 38")
            print("Contact Details: 0875641223")
            print("Gender: Female")
            print("Identity Number: 1234")
            print("Patient Address: 96 Main Rd lytenville")
            print("Next Of Kin: John Rodriguez")
            print("File Number: mhg12")
            print("Patient Room Number: 23")
            print("Patient Admission Date: 21 Nov 2021")
            print("Expected date of death: 20 Dec 2021")
            print("Days Left To Live: 31")
            print("sickness List: Cancer,Type 2 Diabetes")
            print("Prescribed Medication: ") #google types of meds for cancer and type 2 diabetes
            print("")
            print(" ")
            print(" ")


        elif unique_id == '2345':
            print("\n")
            print("Name and Surname of patient: John Samuels")
            print("Date Of Birth(yyyy/mm/dt): 1975 august 14")
            print("Contact Details: 0836781675")
            print("Gender: Male")
            print("Identity Number: 2345")
            print("Patient Address: 84 Albertina Sisulu Rd Johannesburg")
            print("Next Of Kin: Peter Samushonga")
            print("File Number: yth56")
            print("Patient Room Number: 24")
            print("Patient Admission Date: 21 Nov 2021")
            print("Expected date of death: 01 Dec 2021")
            print("Days Left To Live: 12")
            print("sickness List: Cervical Cancer")
            print("Prescribed Medication: ") #google types of meds for cancer and type 2 diabetes
            print("")
            print(" ")
            print(" ")
        
        elif unique_id == '3456':
            print("\n")
            print("Name and Surname of patient: Jonas Sam")
            print("Date Of Birth(yyyy/mm/dt): 1994 september 01")
            print("Contact Details: 0716336362")
            print("Gender: Male")
            print("Identity Number: 3456")
            print("Patient Address: 9611 xenon str Nellmapius Pretoria")
            print("Next Of Kin: Peter Samushonga")
            print("File Number: yth56")
            print("Patient Room Number: 24")
            print("Patient Admission Date: 21 Nov 2021")
            print("Expected date of death: 01 Dec 2021")
            print("Days Left To Live: 12")
            print("sickness List: Cervical Cancer")
            print("Prescribed Medication: ") #google types of meds for cancer and type 2 diabetes
            print("")
            print(" ")
            print(" ")
        else:
            print("Wrong unique_id entered.")

# sign_up()
patient_details()