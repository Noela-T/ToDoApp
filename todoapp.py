from datetime import datetime
from datetime import date

tasks={}
def addTask(task,time):
    #converts time to a datetime object to enable sorting of time
    ctime=datetime.strptime(time,"%H:%M")
    tasks[ctime]=task
    #sorts through the dictionary but returns a list object
    sortedtasks=sorted(tasks.items())
    print ("*****MY TO-DO LIST*****")
    for i in sortedtasks:
        print ("  " + i[0].strftime("%H:%M")+" -"+i[1])
    return 0
    
while True:
    name=input("Enter new task: ");
    time=input("Time for task(e.g 19:30): ")
    addTask(name,time)
