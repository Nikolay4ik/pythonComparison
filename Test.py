import csv

def read_csv(nameFile):
    array_csv_file = []
    with open(nameFile, mode='r',newline='',encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            array_csv_file.append(row)
    return array_csv_file
arr1_file={tuple(row) for row in read_csv('file1_test.csv')}
arr2_file={tuple(row) for row in read_csv('file2_test.csv')}
def create_file(arr1_file,arr2_file,nameFile):
    diff_in_file1=arr1_file-arr2_file
    diff_in_file2=arr2_file-arr1_file
    all_diffs = list(diff_in_file1) + list(diff_in_file2)
    diff_rows = [list(row) for row in all_diffs]
    with open(nameFile,mode='w',newline='',encoding='utf-8') as file:
        writer=csv.writer(file)
        for i in diff_rows:
            writer.writerow(i)
create_file(arr1_file,arr2_file,'file3.csv')
