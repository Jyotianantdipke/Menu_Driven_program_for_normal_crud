from StudentSet import *
 


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
                    pin=int(input(f"Enter pincode of city {i+1} : "))
                    city=input(f"Enter city {i+1} : ")
                    a1.set_city(city)
                    a1.set_pincode(pin)
                    citydict.update({a1.get_pincode():a1.get_city()}) 
                print(citydict,len(citydict))

            elif ch1==2:
                pin=int(input("Enter pincode u want to change name : "))
                for k,v in citydict.items():
                    print(f'{k} {v}')
                    if pin==k:
                        new_name=input("Enter name for new city : ")
                        a1.set_city(new_name)
                        citydict[k]=a1.get_city()  
                print("\n Address Updated")

            elif ch1==3:
                pin=int(input("\nEnter pincode u want to Delete : "))
                del citydict[pin]
                print(f'Deleted {k}')
            
                

            elif ch1==4:
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
                    no_of_student=int(input("\nEnter no of student u want to add : "))
                    for i in range(no_of_student):
                        while True:
                            address1=int(input("Enter pincode :"))
                            if len(citydict) > 0:
                                if address1 in citydict.keys():
                                    add1=[address1,citydict[address1]]
##                                    print('address inserted',add1)
                                    s1.set_address(add1)
##                                    print(s1.get_address())
                                else:
                                    print("No Address Available do u want to insert : "\
                                          "\n1.Yes"\
                                          "\n2.No")
                                    yes_or_no=int(input("Enter Choice for yes or no: "))
                                    if yes_or_no==1:
                                        pin=int(input(f"Enter pincode of city {i+1} : "))
                                        city=input(f"Enter city {i+1} : ")
                                        city1=a1.set_city(city)
                                        pin1=a1.set_pincode(pin)
                                        citydict.update({a1.get_pincode():a1.get_city()})
                                    else:
                                        print("Select Another Pincode")
                            else:
                                print("Insert Address First, no cities Available")
                                pin=int(input(f"Enter pincode of city {i+1} : "))
                                city=input(f"Enter city {i+1} : ")
                                city1=a1.set_city(city)
                                pin1=a1.set_pincode(pin)
                                citydict.update({a1.get_pincode():a1.get_city()})
                                break
                            break       
                        rn=int(input("Enter Roll no: "))
                        name=input("Enter Name: ")
                        mark=int(input("Enter Marks: "))
                        s1.set_rn(rn)
                        s1.set_name(name)
                        s1.set_marks(mark)
                        studentdict.update({s1.get_rn():[s1.get_name(),s1.get_marks(),s1.get_address()]})
                        
##                    print(studentdict)

            elif ch1==2:
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
                        new_name=input("Enter New name")
                        for k,v in studentdict.items():
                            if k==rn:
                                v[0]=new_name

                    elif ch2==2:
                        new_mark=int(input("Enter New marks"))
                        for k,v in studentdict.items():
                            if k==rn:
                                v[1]=new_mark
                    elif ch2==3:
                        print("Currently available cities")
                        for k,v in citydict.items():
                            print(f'{k} : {v}')
                        new_address=int(input("Select pincode form Currently available cities for chnaging address"))
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
                rn=int(input("\nEnter Roll no u want to Delete : "))
                del studentdict[rn]
                print(f'Deleted {rn}')
            
                

            elif ch1==4:
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
                
                
       
