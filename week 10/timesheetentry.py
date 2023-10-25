class Timesheetentry:

    def __init__(self, project, start, duration) :
        self.project = project
        self.start = start
        self.duration = duration
    
    def __str__(self) :
        return self.project + ':' + str(self.duration)
    
import datetime as dt

if __name__ == '__main__':
    ts = dt.datetime(2023, 4, 16, 19, 20)
    test = Timesheetentry('test', ts, 60)
    print (test)


    #Timesheetentry1 = Timesheetentry('Lab', 'now','20')

#print(Timesheetentry1.project)