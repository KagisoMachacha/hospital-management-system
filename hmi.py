# username_list = []
# password_list = []


# print("********************************************************************************************")
# print("*                                                                                          *")
# print("*                   Welcome To Louis Pasture Hospital Management System                    *")
# print("*                                                                                          *")
# print("********************************************************************************************")


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

    


# def patient_details():
#     while True:
#         unique_id = input("please enter patient's unique code to retrieve their details.\n")
#         if unique_id == 1234:
#             print("Name and Surname of patient: Julia Pedro")
#             print("Date Of Birth(yyyy/mm/dt): 1984 may 23")
#             print("Contact Details: 0875641223")
#             print("Gender: Female")
#             print("Identity Number: 1234")
#             print("Patient Address: 96 Main Rd lytenville")
#             print("Next Of Kin: John Rodriguez")
#             print("File Number: mhg12")
#             print("Patient Room Number: 23")
#             print("Patient Admission Date: 21 Nov 2021")
#             print("Days Left To Live: 20 Dec 2021")
#             print("sickness List: Cancer,Type 2 Diabetes")
#             continue
#         else:
#             print("Wrong unique_id entered.")


# def program_exec():
#     sign_up()
#     # patient_details()


# if __name__ == '__main__':
#     program_exec()

print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")