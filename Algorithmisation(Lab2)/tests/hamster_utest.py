import unittest
from manager import hamster_evaluator as ev
from main import BS_and_Quickselect
from additional_files import hamster_reader as reader

class HamsterTest(unittest.TestCase):
    def get_hamsters_from_file(self,filename):
        output = reader.read_info_from_file(filename)
        return output


    def test_Partition(self):
        output= self.get_hamsters_from_file("C:\\Users\\111\\PycharmProjects\\Algorithmisation(Lab2)\\additional_files\\hamster.in.txt")
        hamsters_list = output[0]
        pivot_to_check=ev.Partition(hamsters_list, 0, len(hamsters_list) - 1, 4)
        hamsters_total_consumption=[]
        for hamster in hamsters_list:
            hamsters_total_consumption.append(hamster.calculate_total_food_consumption(4))
        expected_list=[17,17,25,17,18,30]
        self.assertEqual(expected_list,
        hamsters_total_consumption)
        self.assertEqual(0,pivot_to_check)

    def test_QuickSelect(self):
        output= self.get_hamsters_from_file("C:\\Users\\111\\PycharmProjects\\Algorithmisation(Lab2)\\additional_files\\hamster.in.txt")
        hamsters_list = output[0]
        ev.QuickSelect(hamsters_list, 0, len(hamsters_list) - 1, 4)
        hamsters_total_consumption=[]
        for hamster in hamsters_list:
            hamsters_total_consumption.append(hamster.calculate_total_food_consumption(4))
        expected_list=[17,17,17,18,25,30]
        self.assertEqual(expected_list,
        hamsters_total_consumption)

    def test_BS_and_QuickSelect(self):
        output = self.get_hamsters_from_file("C:\\Users\\111\\PycharmProjects\\Algorithmisation(Lab2)\\additional_files\\hamster.in1.txt")
        hamsters_list = output[0]
        total_food_amount = output[1]
        total_hamsters_number = output[2]
        expected_value=9
        total_nuber_of_hamsters=BS_and_Quickselect(hamsters_list,total_food_amount)
        self.assertEqual(expected_value,
                         total_nuber_of_hamsters)
