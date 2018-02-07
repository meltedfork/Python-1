calls_record=[]

class call(object):
    
    def __init__(self,id,name,number,time,reason):
        self.id=id
        self.name=name
        self.number=number
        self.time=time
        self.reason=reason
        calls_record.append(self)

    def display_all(self):
        print self.id
        print self.name
        print self.number
        print self.time
        print self.reason
        return self

class callCenter(object):
    
    def __init__(self,call_list=[],queue=0):
        self.call_list=call_list
        self.queue=queue

    def add_call(self,newCall):
        self.call_list.append(newCall)
        self.queue=len(self.call_list)
        print "New caller added to queue."
        print "Queue is now at", self.queue,"callers."
        return self

    def removeFirst(self):
        self.call_list.pop[0]
        self.queue=len(self.call_list)
        print "Caller removed from queue."
        print "Queue is now at", self.queue,"callers."
        return self

    def info(self):
        print "Current info for callers in queue"
        for callers in self.call_list:
          print callers.name
            # print callers.name
            # print callers.number
        return self


BinghamClinic=callCenter()


call1=call(27,"Kelly","640-298-2999","5:05 A.M.","Murder")
call2=call(45,"Joseph","757-858-8888","1:30 P.M.","I also murdered someone")
call3=call(87,"Dan","848-848-3939","4:30 P.M","I'm being murdered!!!")
call4=call(88,"Joseph","757-858-8888","5:02 P.M","I am murdering again.")

call1.display_all()
call2.display_all()
call3.display_all()
call4.display_all()



BinghamClinic.add_call(call1).add_call(call2).add_call(call3).info().removeFirst().removeFirst().add_call(call4).removeFirst().info()


