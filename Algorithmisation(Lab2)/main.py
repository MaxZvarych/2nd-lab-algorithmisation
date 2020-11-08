from additional_files.hamster_reader import read_info_from_file
from additional_files.hamster_writer import write_answer_to_file
from manager import hamster_evaluator as ev

def BS_and_Quickselect(hamsters_list,total_food_amount):
    if(len(hamsters_list)!=0):
        left=1
        right=len(hamsters_list)
        while(left<=right):
            number_of_hamsters_to_check=(right+left)//2
            total_food_consumption = 0
            ev.QuickSelect(hamsters_list,0,len(hamsters_list)-1,number_of_hamsters_to_check)
            for i in range(0,number_of_hamsters_to_check,1):
                total_food_consumption+=hamsters_list[i].calculate_total_food_consumption(number_of_hamsters_to_check)
            if(total_food_consumption>total_food_amount):
                number_of_hamsters_to_check -= 1
                right=number_of_hamsters_to_check
            else:
                left = number_of_hamsters_to_check+1
    return number_of_hamsters_to_check

if __name__ == '__main__':
    filename = input("Please write filename to get data:")
    #C:\Users\111\PycharmProjects\Algorithmisation(Lab2)\additional_files\hamster.in.txt
    output=read_info_from_file(filename)
    hamsters_list=output[0]
    total_food_amount=output[1]
    total_hamsters_number=output[2]
    result= BS_and_Quickselect(hamsters_list,total_food_amount)
    print(result)
    write_answer_to_file(result)


