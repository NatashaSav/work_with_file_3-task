import glob
import os


def read_files(list_of_files):
    all_files = list()
    for file_name1 in list_of_files:
        f = open(file_name1, 'r')
        lines = f.readlines()
        file_info = dict()
        file_info['file_name'] = os.path.basename(file_name1)
        file_info['len_str'] = len(lines)
        file_info['content'] = lines
        all_files.append(file_info)
    return all_files


def sorted_files(all_files):
    return sorted(all_files, key=lambda file_info: (file_info['len_str']))


def write_in_file(list_files):
    with open('result.txt', 'w') as file:
        for item in list_files:
            file.write('{}\n{}\n{}\n\n'.format(item['file_name'], item['len_str'], ''.join(item['content'])))


def main():
    list_of_files = glob.glob('/Users/dmitro/Documents/Courses/work_with_file/work_with_file_3-task/sorted/*.txt')
    list_files = read_files(list_of_files)
    sorted = sorted_files(list_files)
    write_in_file(sorted)


if __name__ == "__main__":
    main()