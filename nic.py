import nicfunc
nic=""

    


nic_num = input("enter the id number")
print("the nic type is",nicfunc.nic(nic_num))
if 'v' in nic_num:
    print("voter")
if 'x' in nic_num:
    print("non - voter")
if len(nic_num)==12:
    print("all can vote")

gender = int(nic_num[2:5])
if 1<gender<366:
    print("male")
if 501<gender<866:
    print("female")
if len(nic_num)==10:
    birth_year=int(nic_num[0:2])
    print(birth_year)
if len(nic_num) == 12:
    birth_year=int(nic_num[0:4])
    print(birth_year)
                   
    

