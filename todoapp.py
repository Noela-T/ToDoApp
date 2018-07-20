from datetime import datetime
from datetime import date

#indexDict creates a dictionary to match tasks by their their dates to their
#index numbers printed when listing them. This enables tasks to be easily deleted
#by referencing their index numbers.
indexDict={}
timeDict={}
tasks={}
index = 1
#adds a new item to To-Do list
def addTask(task,time):
    global index
    #converts time to a datetime object to enable sorting of time
    tasks[index]=task
    timeDict[timevalue]=index
    index += 1

#lists the items on To-Do list
def listTasks():
    #indexD is a variable used to list the items so they can be easily accesssible
    #from their index numbers when listed
    global indexD
    indexD = 1
    #sorts through the dictionaries but returns a list object
    sortedtasks=sorted(tasks.items())
    sortedtime=sorted(timeDict.items())
    #adding values to indexDict
    for i in sortedtime:
        indexDict[indexD]=i[0]
        indexD += 1
    #Printing out to do list
    print ("*****MY TO-DO LIST*****")
    if tasks == {}:
        print ("\n\n\n<EMPTY TO-DO LIST>\n\n\n")
    for i in sortedtime:
        for j in sortedtasks:
            if (i[1]==j[0]):
                for key, value in indexDict.items():
                    if (i[0]==indexDict[key]):
                        print ("  "+str(key)+". " + i[0].strftime("%H:%M")+" -" + j[1])
    return 0

def deleteTask(num):
    global indexD
    for key, value in indexDict.copy().items():
        if (num == key):
            for timekey, value in timeDict.copy().items():
                if (timekey==indexDict[key]):
                    for taskkey, value in tasks.copy().items():
                        if (taskkey==timeDict[timekey]):
                            del tasks[taskkey]
                    del timeDict[timekey]
            del indexDict[key]
    indexD -= 1


while True:
    global deleteinput
    task=input("Enter new task: ");
    try:
        timeinput=input("Time for task(e.g 19:30): ")
        print ("\n")
        timevalue=datetime.strptime(time,"%H:%M")
    except ValueError:
        print ("Please enter a valid 24-hour time format as shown in the example.")
    else:
        addTask(task,timevalue)
        listTasks()
        print ("\n")
        deleteinput=input("Delete any completed task? yes/no : ")
        if deleteinput == 'yes':
            test= True
            while test:
                try:
                    numToDelete=int(input("Enter task number: "))
                    if numToDelete > indexD:
                        raise ValueError
                except ValueError:
                    print ("Please enter a Valid Task number that exists on To-Do List.")
                else:
                    test = False
                    deleteTask(numToDelete)
                    listTasks()
