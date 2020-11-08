def write_answer_to_file(answer):
    number_of_hamsters=str(answer)
    file=open('additional_files\hamster.out.txt','w')
    file.write(number_of_hamsters)


