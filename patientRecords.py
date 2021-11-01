
from tkinter import *
from date_time import * 
from time import ctime


"""This code was wirtten by me and no other sources were used"""
def main():
    #print data of appointments using external text file
    file = ("Patients Scheduled")
    print(file)
    f = open("patientsScheduled.txt", "r")
    print(f.read())
    print("------------------------------")


    #dictionary with keys(names) and values(appointment time) of scheduled patients
    
    queueDictionary = {"Aaron_Rodgers" : "appointment time = 9:00 am",
                       "Serena_Williams" : "appointment time = 10:45 am",
                       "Macy_Markus" : "appointment time = 2:30 pm",
                       "Mark_Winston" : "appointment time = 6:00pm"}
    

    #asks user to input name
    patient = input("Name of patient: ")

    #input goes through if-else statement to check if the name is listed in dictionary or is a new name
    if(patient.lower() == "aaron rodgers" or patient.lower() == "aaron"):
        #get value for the given key
        aaron = queueDictionary.get("Aaron_Rodgers")
        print(aaron)
        #go to def database() to record patients' data
        database()
        

    elif(patient.lower() == "serena williams" or patient.lower() == "serena"):
        serena = queueDictionary.get("Serena_Williams")
        print(serena)
        database()
    
    elif(patient.lower() == "Macy Markus" or patient.lower() == "macy"):
        macy = queueDictionary.get("Macy_Markus")
        print(macy)
        database()
       

    elif(patient.lower() == "Mark Winston" or patient.lower() == "mark"):
        mark = queueDictionary.get("Mark_Winston")
        print(mark)
        database()

    else:
        #statement for if the patient is not listed in dictionary
        newPatient = input("New Patient? ")
        #verify input
        verify_newPatient = input("You would like to register as {}? ".format(patient))
        if (verify_newPatient == "yes"):
            queueDictionary[patient] = ctime()
           
            
            print("Okay {}, we will begin your paperwork...".format(patient))
            #add new patient to dictionary
            print(patient,":", queueDictionary[patient])
            database()


def database():
    #creates window
    window = Tk()
    window.title("Georgia Hospital")
    window.geometry("750x750+0+0")  


    title = Label(window, text="Georgia Hospital Records", font=("Courier", 30), background="azure3", width=75, height=2)
    title.pack()

    time = Label(window, text = ctime())
    time.pack()
    
    namelbl = Label(text="Name")
    namelbl.pack()
    nameEntry = Entry()
    nameEntry.pack()

    #creates check boxes on window
    male = Checkbutton(window, text="male")
    male.pack()
    female = Checkbutton(window, text="female")
    female.pack()

    #creates frame within window where the text in the frame can be placed on certain sides
    frame = Frame(window)
    frame.pack()

    bottomframe = Frame(window)
    bottomframe.pack( side = BOTTOM )

    dateofBirth = Label(frame, text="Date of Birth")
    dateofBirth.pack(side = LEFT)

    inputDateofBirth = Entry(frame, text=0, width=10)
    inputDateofBirth.pack(side = LEFT)

    inputbirthExample = Label(frame, text="Ex:01/01/2000")
    inputbirthExample.pack(side = BOTTOM)

    space = Label(window, text="  ")
    space.pack()

    #gives user ability to record their symptoms in a box using entry()
    symptoms = Label(window, text="Briefly describe your symptoms: ")
    symptoms.pack()

    symptomsInput = Entry(width=70)
    symptomsInput.pack()

    
    space = Label(window, text="  ")
    space.pack()


    coronaLabel = Label(window, text = "COVID-19 Symptoms")
    coronaLabel.pack()
    
    #list of all the symptoms user may check
    coronaSymptoms = ['fever or chills', 'cough', 'shortness of breath', 'fatigue', 'nausea', 'muscle pain', 'loss of tase or smell']
    coronaCheck = []
    var = [] 
    
    numOfSymptoms = len(coronaSymptoms)

    #for loop that adds to list and creates checkbuttons for each value added to the list
    for i in range(numOfSymptoms):
        coronaCheck.append("")
        var.append(IntVar())
        coronaCheck[i] = Checkbutton(window, text = "Are you experiencing a {}?".format(coronaSymptoms[i]), variable = var[i], onvalue = 1)
        coronaCheck[i].pack()

    

    submit = Button(window, text = "Submit", command = lambda: record(inputDateofBirth, symptomsInput, coronaCheck, numOfSymptoms, var, window))
    submit.pack()
    #calls main method
    NewForm = Button(window, text = "New Form", command = lambda: [window.destroy(), main()])
    NewForm.pack()
    window.mainloop()


def record(DOB, symptomsInput, coronaCheck, length, variables, window):
    dateOfBirth = DOB.get()

    descriptionOfSymptoms = symptomsInput.get()

    #empty list that will hold values of checked symptoms
    symptomCheck = []
    
    for i in range(length):
        symptomCheck.append(variables[i].get())


    print(symptomCheck)
    checkSum = sum(symptomCheck)
    print(checkSum)
    #if user checked more than 3 symptoms, they will be displayed with a "Get tested for corona!" message
    if checkSum>3:
        print("Get tested for corona!")
        checkSumPositive = Label(window, text = "Get tested before your appointment!", fg="red")
        checkSumPositive.pack()

    #if user checked less than 3 symptoms, they will be displayed with a "Carry on to your appointment." message
    else:
        checkSumNegative = Label(window, text = "Carry on to your appointment.", fg="red")
        checkSumNegative.pack()
        
           

        

if (__name__ == "__main__"):
    main()
