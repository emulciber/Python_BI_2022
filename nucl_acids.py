dna_to_rna = {'A': 'U', 'a': 'u', 'T': 'A', 't': 'a', 'G': 'C', 'g': 'c', 'C': 'G', 'c': 'g'}
rna_to_dna = {'A': 'T', 'a': 't', 'u': 'A', 'U': 'a', 'G': 'C', 'g': 'c', 'C': 'G', 'c': 'g'}
dna_to_dna = {'A': 'T', 'a': 't', 'T': 'A', 't': 'a', 'G': 'C', 'g': 'c', 'C': 'G', 'c': 'g'}
rna_to_rna = {'A': 'U', 'a': 'u', 'U': 'A', 'u': 'a', 'G': 'C', 'g': 'c', 'C': 'G', 'c': 'g'}


def check_sequence(seq):
    seq_check = seq.upper()

    if seq_check.count('A') + seq_check.count('T') + seq_check.count('G') + seq_check.count('C') == len(seq_check):
        return 'DNA'
    elif seq_check.count('A') + seq_check.count('U') + seq_check.count('G') + seq_check.count('C') == len(seq_check):
        return 'RNA'
    else:
        print('Некорректная последовательность. Программа принимает только последовательности ДНК или РНК')
        return 'Error'
        

def transcribe(seq, seq_type):   # напечатать транскрибированную последовательность
    new_seq_list = []

    for nucl in seq:
        if seq_type == 'DNA':
            new_seq_list.append(dna_to_rna[nucl])
        elif seq_type == 'RNA':
            new_seq_list.append(rna_to_dna[nucl])

    return ''.join(new_seq_list)


def reverse(seq):      # напечатать перевёрнутую последовательность
    return seq[::-1]


def complement(seq, seq_type):   # напечатать комплементарную последовательность
    new_seq_list = []
    for nucl in seq:
        if seq_type == 'DNA':
            new_seq_list.append(dna_to_dna[nucl])
        elif seq_type == 'RNA':
            new_seq_list.append(rna_to_rna[nucl])

    return ''.join(new_seq_list)


def reverse_complement(seq, seq_type):   # напечатать обратную комплементарную последовательность
    new_seq_list = []
    for nucl in seq:
        if seq_type == 'DNA':
            new_seq_list.append(dna_to_dna[nucl])
        elif seq_type == 'RNA':
            new_seq_list.append(rna_to_rna[nucl])

    return ''.join(new_seq_list[::-1])




if __name__ == '__main__':
    while True:
        command = input('Введите команду: ')

        if command == 'exit':
            print('Работа программы завершена.')
            break
        elif command not in ['transcribe', 'reverse', 'complement', 'reverse complement']:
            print('Вы ввели неверную команду. Доступны следующие команды: transcribe, reverse, complement, reverse complement, exit')
            continue

        seq = input('Введите последовательность: ')
        
        seq_type = check_sequence(seq)
        if seq_type == 'Error':
            continue

        if command == 'transcribe':
            new_seq = transcribe(seq, seq_type)
            print('Транскрибированная последовательность:', new_seq)

        elif command == 'reverse':
            new_seq = reverse(seq)
            print('Перевернутая последовательность:', new_seq)

        elif command == 'complement':
            new_seq = complement(seq, seq_type)
            print('Комплементарная последовательность:', new_seq)

        elif command == 'reverse complement':
            new_seq = reverse_complement(seq, seq_type)
            print('Перевернутая комплементарная последовательность:', new_seq)
        
        else:
            print('Что-то пошло не так. Попробуйте еще раз')
            continue
        

