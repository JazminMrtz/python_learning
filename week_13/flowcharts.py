#Main import of data 
import student_data
students = student_data.students

# Problem 1: Update a students name:----------------------------------------------------------------------------------
#asks for a students id
CPS_ID= int(input("What's your CPS ID?"))
found= False

for student in students:    
    if CPS_ID == student ["CPSID"]:  #This section is to see if the student exist within the database
        new_fname = input ("What's your first name?")  #Asks for a students first name
        new_lname= input ("What's your last name?")  #Asks for a students last name
        student['FName'] = new_fname  #Updates their first name
        student['LName'] = new_lname  #Updates their last name
        found=True
        #Displays their updated name
        print (['FName'])
        print (['LName'])
        #ends the loop so it doesn't continue forever
        break
    
if not found:
    print ("Student not found")  #Only displays when a student doesn't appear in the database
    

# Problem 2: Delete the MName key for a student based on CPSID--------------------------------------------------------

cps_id = int(input("What is your CPS id?")) #asks user for their CPSID
found=False

for student in students:
    if cps_id == student['CPSID']: #finds student in student database
        del student['MName']  #delets middle name
        print(f"Updated student: {student}") #updates their name without their middle name
    else:
        print("Student not found.") #if student is not found


if not found:
    print("CPSID was not found.") #tells user if student is not found 