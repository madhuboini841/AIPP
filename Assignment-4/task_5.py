def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

if __name__ == "__main__":
    file_path = 'task_5.txt'
    line_count = count_lines_in_file(file_path)
    print(f'The file contains {line_count} lines.')