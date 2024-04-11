file_list = ['1.txt', '2.txt', '3.txt']


def get_rows_count(files_name):
    with open(files_name, encoding='utf-8') as f:
        list_line = [line.strip() for line in f]
        list_count = []
        for n in list_line:
            list_count.append(n)
        return len(list_count)


def get_text(files_name):
    with open(files_name, encoding='utf-8') as f:
        list_line = [line.strip() for line in f]
        full_text = ''
        for n in list_line:
            full_text += (n + '\n')
        return [full_text]


def get_common_list():
    all_elements_list = []
    for name in file_list:
        for count in str(get_rows_count(name)):
            for text in get_text(name):
                all_elements_list.append([name, count, text])
    return all_elements_list


sort_list = sorted(get_common_list(), key=lambda text: text[1])


def get_sort_string():
    sort_string = ''
    for i in sort_list:
        for n in i:
            if n != i[-1]:
                sort_string += n + '\n'
            else:
                sort_string += n
    return sort_string


with open('common_file.txt', 'w', encoding='utf-8') as w:
    w.write(get_sort_string())
