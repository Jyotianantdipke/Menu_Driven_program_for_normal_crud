from StudentSet import *

class InvalidInput(Exception):
    def __init__(self,msg):
        self.msg=msg

def len_pincode(pincode):
    count=0
    while pincode>0:
        count+=1
        pincode=pincode//10
    return count


def add_pincode_check(pin):
    if len_pincode(pin)>6 or len_pincode(pin)<6:
        raise InvalidInput("Pincode should be 6 digits only")

    else:
        return pin

def check_pincode(pin):
    if pin not in citydict.keys():
        raise InvalidInput("This city is not available please select Another pincode ")
    else:
        return pin
    
    
        

def check_marks(mark):
    if mark > 100 or mark <= 0:
        raise InvalidInput("Marks must not be less than zero or greater than 100")
    else:
        return mark


citydict=dict()
studentdict=dict()
while True:
    ch=int(input("----select operation----"\
                 "\n1.Address"\
                 "\n2.Student"\
                 "\n3.Exit"\
                 "\nEnter your choice for operation : "))
    if ch==1:
        while True:
            ch1=int(input("\n1.Create Address"\
                          "\n2.Update Address"\
                          "\n3.Delete Address"\
                          "\n4.Show Address"\
                          "\n5.Exit"\
                          "\nEnter your choice: "))
            if ch1==1:
                no_of_address=int(input("Enter no of cities u want to add : "))
                for i in range(no_of_address):
                    while True:
                        try:
                            pin=add_pincode_check(int(input(f"Enter pincode of city {i+1} : ")))
                            break
                        except (ValueError,InvalidInput) as e:
                            print(e)
                    city=input(f"Enter city {i+1} : ")
                    a1.set_city(city)
                    a1.set_pincode(pin)
                    citydict.update({a1.get_pincode():a1.get_city()}) 
                print(citydict,len(citydict))

            elif ch1==2:
                if len(citydict)==0:
                    print("No addresses Available ")
                else:
                    while True:
                        try:
                            pin=check_pincode(int(input("Enter pincode u want to change: ")))
                            break
                        except (InvalidInput) as e:
                            print(e)
                    for k,v in citydict.items():
                        print(f'{k} {v}')
                        if pin==k:
                            new_name=input("Enter name for new city : ")
                            a1.set_city(new_name)
                            citydict[k]=a1.get_city()  
                    print("\n Address Updated")

            elif ch1==3:
                    while True:
                        try:
                            pin=check_pincode(int(input("Enter pincode: ")))
                            print(pin)
                            break
                        except (InvalidInput) as e:
                            print(e)
                    print(citydict)
                    del citydict[pin]
                    print(f'Deleted {k}')
            
                

            elif ch1==4:
                if len(citydict)==0:
                    print("No addresses Available ")
                else:
                    for k,v in citydict.items():
                        print(f"{k} : {v}")

            elif ch1==5:
                break

            else:
                print("\n Wrong choice")
                          
                            
    elif ch==2:           
        while True:
            ch1=int(input("1.Create Student"\
              "\n2.Update Student"\
              "\n3.Delete Student"\
              "\n4.Show Student"\
            "\n5.Show student by descending marks "\
              "\n6.Exit"\
            "\nEnter your choice: "))
            if ch1==1:
                if len(citydict)==0:
                    print("No cities available please add city first")
                    pin=add_pincode_check(int(input("Enter pincode of city : ")))
                    city=input("Enter city : ")
                    a1.set_city(city)
                    a1.set_pincode(pin)
                    citydict.update({a1.get_pincode():a1.get_city()})
                    print(f"\n{a1.get_pincode()} {a1.get_city()} added successfully")

                no_of_students=int(input("Enter no of student u want to add: "))
                for i in range(no_of_students):
                    rn=int(input("Enter Roll no: "))
                    name=input("Enter Name: ")
                    while True:
                        try:
                            mark=check_marks(int(input("Enter Marks: ")))
                            break
                        except InvalidInput as e:
                            print(e)
                    while True:
                        try:
                            address=check_pincode(int(input("Enter pincode: ")))
                            break
                        except (InvalidInput) as e:
                            print(e)
                            
                    s1.set_rn(rn)
                    s1.set_name(name)
                    s1.set_marks(mark)
                    if address in citydict.keys():
                        add1=[address,citydict[address]]
                        s1.set_address(add1)

                    studentdict.update({s1.get_rn():[s1.get_name(),s1.get_marks(),s1.get_address()]})
                    

                        
                        
                    
                        


            elif ch1==2:
                if len(studentdict)==0:
                    print("No students Available ")
                else:
                    rn=int(input("Enter roll no u want to update the data: "))
                    for k,v in studentdict.items():
                        if k==rn:
                            print(f"{k}---->{v}")


                    while True:
                        ch2=int(input("----select operation for student info update----"\
                                     "\n1.change name"\
                                     "\n2.change marks"\
                                     "\n3.change address"\
                                     "\n4.Exit"\
                                     "\nEnter your choice for operation : "))
                        if ch2==1:
                            new_name=input("Enter New name: ")
                            for k,v in studentdict.items():
                                if k==rn:
                                    v[0]=new_name

                        elif ch2==2:
                            new_mark=int(input("Enter New marks: "))
                            for k,v in studentdict.items():
                                if k==rn:
                                    v[1]=new_mark
                        elif ch2==3:
                            
                            print("Currently available cities")
                            for k,v in citydict.items():
                                print(f'{k} : {v}')
                            while True:
                                try:
                                    new_address=check_pincode(int(input("Select pincode form Currently available cities for changing address: ")))
                                    break
                                except (InvalidInput) as e:
                                    print(e)
                            for k,v in studentdict.items():
                                for k1,v1 in citydict.items():
                                    if k1==new_address:
                                        v[2][0]=new_address
                                        v[2][1]=citydict[k1]                       
                                

                            
                        elif ch2==4:
                            break

                        else:
                            print("Wrong Choice")
                                    
                            
                        

            elif ch1==3:
                if len(studentdict)==0:
                    print("No students Available ")
                else:
                    rn=int(input("\nEnter Roll no u want to Delete : "))
                    del studentdict[rn]
                    print(f'Deleted {rn}')
            
                

            elif ch1==4:
                if len(studentdict)==0:
                    print("No students Available ")
                else:
                    for k,v in studentdict.items():
                        print(f"{k}---->")
                        for i in v:
                            print(i)


            elif ch1==5:
                marks_list=[]
                for v in studentdict.values():
                    marks_list.append(v[1])

                    
                new_list=sorted(marks_list)
                print(new_list)
                
                for i in reversed(new_list):
                    for k,v in studentdict.items():
                        if i==v[1]:
                            print(f'{k} : {v}')

            elif ch1==6:
                break

            else:
                print("\n Wrong choice")
                
                
       
                
       
