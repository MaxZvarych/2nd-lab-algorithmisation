from Hamster import Hamster
def read_info_from_file(filename):
    total_food_amount=0
    total_hamsters_number=0
    list_of_hamsters= []
    hamsters = open(filename,'r')
    i=0
    for row in hamsters:
        if(i!=0 and i!=1):
            hamster_info=row.split()
            list_of_hamsters.append(Hamster(int(hamster_info[0]), int(hamster_info[1])))
        elif(i==0) :
            total_food_amount=int(row)
            i += 1
        else:
            total_hamsters_number = int(row)
            i += 1
    return list_of_hamsters,total_food_amount,total_hamsters_number

