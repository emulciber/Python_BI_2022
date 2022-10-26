def filter_gc(read, gc_bounds):
    if type(gc_bounds) != tuple:
        gc_bounds = (0, gc_bounds)
    read_gc = (read[1].count('G') + read[1].count('C')) / len(read[1]) * 100
    return read_gc >= gc_bounds[0] and read_gc <= gc_bounds[1]


def filter_quality(read, quality_treshold):
    sum_quality = 0
    for symbol in read[3]:
        sum_quality += (ord(symbol) - 33)
    read_quality = sum_quality / len(read[3])
    return read_quality >= quality_treshold


def filter_length(read, length_bounds):
    if type(length_bounds) != tuple:
        length_bounds = (0, length_bounds)
    read_length = len(read[1])
    return read_length >= length_bounds[0] and read_length <= length_bounds[1]


def write_files(read, checkings, save_filtered, file_output_passed, file_output_failed):
    if checkings:
        file_output_passed.write(''.join([string+'\n' for string in read]))
    else:
        if save_filtered == True:
            file_output_failed.write(''.join([string+'\n' for string in read]))


def check_read(read, gc_bounds, quality_treshold, length_bounds) -> bool:
    cond1 = filter_gc(read, gc_bounds)
    cond2 = filter_quality(read, quality_treshold)
    cond3 = filter_length(read, length_bounds)
    return all((cond1, cond2, cond3))


def main(input_fastq,
         output_file_prefix='fastq_filtrator_output',
         gc_bounds=(0, 100),
         length_bounds=(0, 2**32),
         quality_treshold=0,
         save_filtered=False):

    file_output_passed_name = f'{output_file_prefix}_passed.fastq'
    file_output_passed = open(file_output_passed_name, 'w')
    if save_filtered:
        file_output_failed_name = output_file_prefix + '_failed.fastq'
        file_output_failed = open(file_output_failed_name, 'w')


    with open(input_fastq) as file_input:

        read = []
        counter = 0

        for line in file_input:
            read.append(line.strip())
            counter += 1

            if counter == 4:
                checkings = check_read(read, gc_bounds, quality_treshold, length_bounds)
                write_files(read, checkings, save_filtered, file_output_passed, file_output_failed)

                read = []
                counter = 0
    
    file_output_failed.close()
    file_output_passed.close()