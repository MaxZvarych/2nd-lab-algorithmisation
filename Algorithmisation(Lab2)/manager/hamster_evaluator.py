from Hamster import Hamster


def Partition(list_of_hamsters, min_idx, max_idx, number_of_hamsters_to_check):
    pivot = min_idx

    for current_element in range(min_idx,max_idx,1):
        if (list_of_hamsters[current_element].calculate_total_food_consumption(number_of_hamsters_to_check) <
                list_of_hamsters[max_idx].calculate_total_food_consumption(number_of_hamsters_to_check)):
            list_of_hamsters[pivot], list_of_hamsters[current_element] = list_of_hamsters[current_element], \
                                                                         list_of_hamsters[pivot]
            pivot += 1
    if(pivot<=max_idx):
        list_of_hamsters[pivot], list_of_hamsters[max_idx] = list_of_hamsters[max_idx], list_of_hamsters[pivot]
    return pivot


def QuickSelect(list_of_hamsters, min_idx, max_idx, quantity_to_check):
    partition = Partition(list_of_hamsters, min_idx, max_idx, quantity_to_check)
    if (partition < quantity_to_check):
        QuickSelect(list_of_hamsters, partition + 1, max_idx, quantity_to_check)
    if(partition>quantity_to_check):
        QuickSelect(list_of_hamsters, min_idx, partition - 1, quantity_to_check)
