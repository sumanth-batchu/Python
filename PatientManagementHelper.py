class PatientManagement:
    def __init__(self):
        self.patient_dict = {}
        self.file_name = input("Enter the file name:")
        self.read_patients_file(self.file_name)

    def read_patients_file(self, file_name):
        count = 0
        try:
            fhand = open(self.file_name, "r")
        except OSError:
            print("File cannot be opened", file_name)
            exit()
        line = fhand.readline()
        while line:
            self.patient_dict[count] = line
            line = fhand.readline()
            count += 1
        print("Loaded", count, "records from file")
        self.main_menu()

    def main_menu(self):
        option = 1
        while option == 1:
            print("###############################################")
            print("#######" + "           MAIN MENU             " + "#######")
            print("###############################################")
            print("#######" + " 1.Add Patient                   " + "#######")
            print("#######" + " 2.View patient at specific index" + "#######")
            print("#######" + " 3.View all patients             " + "#######")
            print("#######" + " 4.Search for Patient            " + "#######")
            print("#######" + " 5.Exit                          " + "#######")
            print("###############################################")
            inside_option = input("Select an input.....")
            if inside_option == '1':
                self.add_patient()
            elif inside_option == '2':
                self.find_patient_at_specific_index(int(input("Enter the index:")))
            elif inside_option == '3':
                self.show_all()
            elif inside_option == '4':
                self.find_patient_with_name()
            elif inside_option == '5':
                count = 0
                fhand = open("output.txt", "w")
                fhand.write("{:20s}{:15s} {:5s} {:2s}".format('NAME', 'SSN', 'AGE', 'DIGNOSIS'))
                fhand.write("\n")
                for k, v in self.patient_dict.items():
                    count += 1
                    line = v
                    name, ssn, age, dia = line.split(',')
                    fhand.write("---------------------------------------------------------")
                    fhand.write("\n")
                    fhand.write('{:20s}{:15s} {:5s} {:2s}'.format(str(name), str(ssn), str(age), str(dia)))
                    fhand.write("\n")
                print("\n")
                print("-------------Total", count, "records loaded into file---------------")
                option = 0
            else:
                print("Invalid option..... ")

    def add_patient(self):
        length = len(self.patient_dict)
        value = ""
        value += input("Enter patient name:")
        value += ","
        value += input("Enter patient SSN:")
        value += ","
        value += input("Enter patient AGE:")
        value += ","
        value += input("Enter patient DIAGNOSIS:")
        self.patient_dict[length + 1] = value
        print("-----------Patient added successfully------------")

    def find_patient_at_specific_index(self, ind_to_returned):
        try:
            line1 = list(self.patient_dict.values())
            line = line1[ind_to_returned]
            name, ssn, age, dia = line.split(',')
            print("{:20s}{:15s} {:5s} {:2s}".format('NAME', 'SSN', 'AGE', 'DIAGNOSIS'))
            print("---------------------------------------------------------")
            print("{:20s}{:15s} {:5s} {:2s}".format(name, ssn, age, dia))
        except:
            print("-------Index out of range--------")

    def show_all(self):
        print("{:20s}{:15s} {:5s} {:2s}".format('NAME', 'SSN', 'AGE', 'DIGNOSIS'))
        for k, v in self.patient_dict.items():
            line = v
            name, ssn, age, dia = line.split(',')
            print("---------------------------------------------------------")
            print('{:20s}{:15s} {:5s} {:2s}'.format(str(name), str(ssn), str(age), str(dia)))

    def find_patient_with_name(self):
        input_name = input("Enter the name to search:")
        count = 0
        for k, v in self.patient_dict.items():
            value = v
            name, ssn, age, dia = value.split(',')
            if name == input_name:
                count += 1
                print("{:20s}{:15s} {:5s} {:2s}".format('NAME', 'SSN', 'AGE', 'DIAGNOSIS'))
                print("---------------------------------------------------------")
                print("{:20s}{:15s} {:5s} {:2s}".format(name, ssn, age, dia))
        if count == 0:
            print("")
            print("------The name entered is not found in the Patients list-------")

pm = PatientManagement()
