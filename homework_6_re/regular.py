import re
import matplotlib.pyplot as plt
import seaborn as sns

def get_ftp(input_file):
    ftp_links = []
    for line in input_file.readlines():
        record = re.split('\t|;', line)
        for substring in record:
            if re.match('ftp.', substring):
                ftp_links.append(substring + '\n')
    return ftp_links


def get_numbers(text):
    numbers_list = re.findall('[0-9]+', text)
    numbers_list = set(numbers_list)
    return numbers_list


def get_a_words(text):
    words_list = re.findall(r'\w*a\w*', text, flags=re.IGNORECASE)
    for index in range(len(words_list)):
        words_list[index] = words_list[index].lower()
    words_list = set(words_list)
    return words_list


def get_exclamations(text):
    exclamation_list = re.findall(r'[A-Z][\w ,\']*!', text)
    return exclamation_list


def get_words_lengths(text):
    words_list = re.findall(r'[a-z\']+', text, flags=re.IGNORECASE)
    for index in range(len(words_list)):
        words_list[index] = words_list[index].lower()
    words_list = set(words_list)
    words_lengths_list = [len(word) for word in words_list]
    return(words_lengths_list)


def translate_to_brick(string):
    pattern = r'([аеёиоуыэюя])'
    repl = r'\1к\1'
    brick_string = re.sub(pattern, repl, string)
    return brick_string


def find_n_word_sentences(one_text, words_number):
    sentences_list = []
    sentences = re.split(r'[.!?]', one_text)
    for sent in sentences:
        words_list = re.split(' ', sent)
        words_list = tuple(filter(bool, words_list))
        if len(words_list) == words_number:
            sentences_list.append(words_list)
    return sentences_list


if __name__ == '__main__':

    # Task 1
    with open('/Users/emulciber/IB/python/Python_BI_2022/homework_6_re/references', 'r') as input_file:
        with open('/Users/emulciber/IB/python/Python_BI_2022/homework_6_re/ftps', 'w') as output_file:
            ftps = get_ftp(input_file)
            output_file.writelines(ftps)

    # Task 2
    with open('/Users/emulciber/IB/python/Python_BI_2022/homework_6_re/2430AD.txt', 'r') as text:
        text = text.read()
        numbers_list = get_numbers(text)
        print(f'Task 2 - all numbers in text is:','\n', *numbers_list)

        print('\n')

    # Task 3
        a_words = get_a_words(text)
        print(f'Task 3 - all words with a in word is:', '\n', *a_words)

        print('\n')

    # Task 4
        exclamation_list = get_exclamations(text)
        print(f'Task 4 - all sentences with an exclamation point is:', *exclamation_list, sep='\n')

        print('\n')

    # Task 5
        words_lengths_list = get_words_lengths(text)
        hist = sns.histplot(words_lengths_list, binwidth = 1).get_figure()
        plt.xlabel('Lengths of unique words')
        hist.savefig('/Users/emulciber/IB/python/Python_BI_2022/homework_6_re/words_lenghts_hist.png')

    # Task 6
    string = 'Кардинальные изменения ландшафта'
    brick_string = translate_to_brick(string)
    print(f'Task 6 - translated string to brick language:', brick_string, sep='\n')

    print('\n')

    # Task 7
    one_text = "Здесь три слова? А здесь не три слова. Здесь тоже три"
    words_number = 3
    n_word_sentences = find_n_word_sentences(one_text, words_number)
    print(f'Task 7 - find n words sentences:', n_word_sentences, sep='\n')
