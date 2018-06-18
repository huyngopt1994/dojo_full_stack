import random
import uuid
class Patient(object):
    def __init__(self, name, allergies):
        """

        :param id: id number of patient
        :param str name: name of patitent
        :param array allergies: array of allergy
        :param int bed_number: the number of patient's bed
        """
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        self.id = None # unique id for per patient

class Hospital(object):
    def __init__(self, name, capacity):
        """

        :param name:
        :param capacity:
        :param patients:
        """
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.beds = []
    def admit(self,patient):
        if len(self.patients) == self.capacity:
            print("Full patients the capacity of this hospital is %s" % self.capacity)
            return
        #create bed_number:
        bed_number = random.randint(0,1000)
        for i in range(15):
            if not bed_number in self.beds:
                self.beds.append(bed_number)
                break
        else:
            raise Exception('Can not get bed number for patient')

        patient.bed_number = bed_number
        patient.id = str(uuid.uuid4())
        self.patients.append(patient)
        print("Add patient name %s")
    def discharge(self,patient_id):
        copy_patients = self.patients[:]
        for i in range(len(copy_patients)):
            if copy_patients[i].id == patient_id:
                self.beds.remove(self.patients[i].bed_number)
                self.patients[i].bed_num = None
                del self.patients[i]

    def display_info(self):
        for i in self.patients:
            print("Patient name %s get %s" % (i.name, i.allergies))

my_hospital = Hospital('vn hospital', 50)
patient_a = Patient('huy',['sick'])
my_hospital.admit(patient_a)
patient_b = Patient('yen',['pain'])
my_hospital.admit(patient_b)

my_hospital.display_info()

my_hospital.discharge(patient_b.id)

my_hospital.display_info()