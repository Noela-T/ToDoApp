from datetime import datetime
from datetime import date

indexDict={}
timeDict={}
tasks={}
index = 1
def addTask(task,time):
    global index
    indexD=1
    #converts time to a datetime object to enable sorting of time
    ctime=datetime.strptime(time,"%H:%M")
    tasks[index]=task
    timeDict[ctime]=index
    index += 1
    #sorts through the dictionaries but returns a list object
    sortedtasks=sorted(tasks.items())
    sortedtime=sorted(timeDict.items())
    for i in sortedtime:
        indexDict[indexD]=i[0]
        indexD += 1
    print ("*****MY TO-DO LIST*****")
    for i in sortedtime:
        for j in sortedtasks:
            if (i[1]==j[0]):
                for key, value in indexDict.items():
                    if (i[0]==indexDict[key]):
                        print ("  "+str(key)+". " + i[0].strftime("%H:%M")+" -" + j[1])
    return 0

def deleteTask(num):
    num=int(num)
    for key, value in indexDict.copy().items():
        if (num == key):
            for timekey, value in timeDict.copy().items():
                if (timekey==indexDict[key]):
                    for taskkey, value in tasks.copy().items():
                        if (taskkey==timeDict[timekey]):
                            del tasks[taskkey]
                    del timeDict[timekey]
            del indexDict[key]

while True:
    name=input("Enter new task: ");
    time=input("Time for task(e.g 19:30): ")
    addTask(name,time)
    deleteinput=input("Delete any completed task? Yes/No : ")
    if deleteinput == 'Yes':
        numToDelete=input("Enter task number: ")
        deleteTask(numToDelete)
