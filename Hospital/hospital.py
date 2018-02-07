import random


class Patient(object):
    
    def __init__ (self,name,allergies):
        self.id=0
        self.name=name
        self.allergies=allergies
        self.bed=0

class Hospital (object):
    
    def __init__(self,hosp_name):
        self.patients=[]
        self.hosp_name=hosp_name
        self.capacity=100
        self.hosp_bed=0
        self.hosp_id=0


    def admit (self,newPatient):
        if len(self.patients) < self.capacity:
            self.patients.append(newPatient)
            self.hosp_id+=1
            self.hosp_bed +=1
            newPatient.bed=self.hosp_bed
            newPatient.id=self.hosp_id
            print "Welcome to",self.hosp_name, "hospital."
            print "There are currently", len(self.patients), "patient(s) in the hospital."
            for patient in self.patients:
                print patient.name, "is in bed number:", self.hosp_bed, ", with id number:", self.hosp_id
            return self
        else:
            print "Sorry, buddy. Scram."
            return self
            

    def discharge(self,exitPatient):
        if len(self.patients) > 0:
            print "Finding patient..."
            for patient in self.patients:
                if patient==exitPatient:
                    print patient.name, "found, giving him the boot."
                    for i in range (0,len(self.patients)):
                        if patient == self.patients[i]:
                            self.patients.pop(i)
                            self.hosp_id-=1
                            self.hosp_bed-=1
        print "There are currently", len(self.patients), "patients in the hospital."
        return self

    def display_info(self):
        print "Status report: There are currently", len(self.patients), "patient(s) in the hospital."
        for patient in self.patients:
            print patient.name, "is in bed number:", self.hosp_bed, ", with id number:", self.hosp_id
        return self


Mercy=Hospital("Mercy")
Jeff=Patient("Jeff","none")
Marge=Patient("Marge","bananas")
George=Patient("George","sunlight")


Mercy.admit(Jeff).discharge(Jeff).admit(Marge).admit(George).discharge(George).display_info().discharge(Marge)
