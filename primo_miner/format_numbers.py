from libs.arq_manipulator import Arq_txt

def format_numbers(arq_path, split_separator, lenth_for_line):
    arq = Arq_txt(arq_path)
    arq_before = arq.get_lines('all')
    line_now = ''
    arq_after = []
    for line in arq_before[0:-1]:
        line_splited = line.split(split_separator)
        line_splited.pop(-1)
        for num in line_splited:
            line_now += num+split_separator
            if len(line_now[0:-1].split(split_separator)) == lenth_for_line:
                line_now+='\n'
                arq_after.append(line_now)
                line_now = ''
    if line_now != '':
        line_now+='\n'
        arq_after.append(line_now)

    arq_after.append(arq_before[-1])
    arq.rewrite_all(arq_after)

    print(f'Arquivo {arq_path} formatado.')

def main():
    #configs--------------------------------
    arq_path = './primos_found.txt'
    split_separator = ','
    number_for_line_before = 10
    #---------------------------------------

    format_numbers(arq_path, split_separator, number_for_line_before)

if __name__ == '__main__':
    main()
