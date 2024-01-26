import re

id_list = []
vehicle_list = []
one = []
two = []
three = []

def remove_vehicle(id):
    for i in one:
        if i.id==id:
            one.remove(i)
            id_list.remove(id)
            vehicle_list.remove(i.vehicleno)
            basement1.space+=1
            return "Vehicle Removed"

    for i in two:
        if i.id==id:
            two.remove(i)
            id_list.remove(id)
            vehicle_list.remove(i.vehicleno)
            basement2.space+=1
            return "Vehicle Removed"

    for i in three:
        if i.id==id:
            three.remove(i)
            id_list.remove(id)
            vehicle_list.remove(i.vehicleno)
            basement3.space+=1
            return "Vehicle Removed"
def add_vehicle(arr):
    if basement1.space>0:
        one.append(basement1(*arr))
        id_list.append(int(arr[0]))
        vehicle_list.append(arr[2])

    elif basement2.space>0:
        two.append(basement2(*arr))
        id_list.append(int(arr[0]))
        vehicle_list.append(arr[2])


    else:
        three.append(basement3(*arr))
        id_list.append(int(arr[0]))
        vehicle_list.append(arr[2])
def check_validity(arr):
    if len(arr)<4:
        print("Enter All values")
        return False
    try:
        id = int(arr[0])
        if id in id_list:
            print("ID already present")
            return False
    except ValueError as e:
        print("Enter ID as integer")
        return False

    if (arr[3]!='fw') and (arr[3]!='tw'):
        print("Enter valid vehicle type")
        return False

    patt = "^[A-Z]{2}[ -]?[0-9]{2}[ -]?[A-Z]{1,2}[ -]?[0-9]{4}$"
    if (re.match(patt,arr[2])) and (arr[2] not in vehicle_list):
      return True
    else:
        print("Vehicle Number doesnt follow conventions or vehicle already present")
        return False
def check_empty():
    if (basement1.space>0) or (basement2.space>0) or (basement3.space>0):
        return True
    else:
        return False

class basement1:
    space = 4
    def __init__(self,id,name,vehicleno,vehicletype,basement=1):
        basement1.space-=1
        self.id = int(id)
        self.name = name
        self.vehicleno = vehicleno
        self.vehicletype = vehicletype
        self.basement = basement
        print("Vehicle at Basement 1")

    def __str__(self):
        return (f"{str(self.id).center(7)}|{str(self.name).center(7)}|{str(self.vehicleno).center(7)}|{str(self.vehicletype).center(7)}|"
                f"{str(self.basement).center(7)}")

class basement2:
    space = 4
    def __init__(self,id,name,vehicleno,vehicletype,basement=2):
        basement2.space-=1
        self.id = int(id)
        self.name = name
        self.vehicleno = vehicleno
        self.vehicletype = vehicletype
        self.basement = basement
        print("Vehicle at Basement 2")

    def __str__(self):
        return (f"{str(self.id).center(7)}|{str(self.name).center(7)}|{str(self.vehicleno).center(7)}|{str(self.vehicletype).center(7)}|"
                f"{str(self.basement).center(7)}")

class basement3:
    space = 4
    def __init__(self,id,name,vehicleno,vehicletype,basement=3):
        basement3.space-=1
        self.id = int(id)
        self.name = name
        self.vehicleno = vehicleno
        self.vehicletype = vehicletype
        self.basement = basement
        print("Vehicle at Basement 3")

    def __str__(self):
        return (f"{str(self.id).center(7)}|{str(self.name).center(7)}|{str(self.vehicleno).center(7)}|{str(self.vehicletype).center(7)}|"
                f"{str(self.basement).center(7)}")


while True:
    print("Select Option")
    print("1. Add Vehicle")
    print("2. Remove Vehicle")
    print("3. Check Basement Occupancy")
    print("4. Quit")
    try:
        option = int(input())

        if option == 1:
            if check_empty():
                values = input().split()
                if check_validity(values):
                    add_vehicle(values)
            else:
                print(f"All Basements Full")


        elif option == 2:
            id = int(input("Enter ID:"))
            if id not in id_list:
                print("No ID present")
            else:
                print(remove_vehicle(id))


        elif option==3:
            try:
                number = int(input("Enter Basement Number:"))
                if number==1:
                    if len(one)==0:
                        print("Empty Basement")
                    else:
                        for i in one:
                            print(i)

                elif number==2:
                    if len(two)==0:
                        print("Empty Basement")
                    else:
                        for i in two:
                            print(i)

                elif number ==3 :
                    if len(three)==0:
                        print("Empty Basement")
                    else:
                        for i in three:
                            print(i)
                else:
                    print("Enter Correct Basement Number")
            except ValueError as e:
                print("Enter Correct Basement Number")


        elif option == 4:
            print("Thank You\n")
            break

        else:
            print("Enter Valid Option")

    except ValueError as e:
        print("Enter Valid Option")

