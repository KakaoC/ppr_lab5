import csv
import os

def create_annotation(subdir:str,label, folderpath) -> None:
    with open("annotation_train.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator='\n')
        for i in range(1020):
            absolute_way = os.path.abspath(f'{folderpath}/train/{subdir}/{str(i).zfill(4)}.jpg')
            if (os.path.isfile(absolute_way)) == True:
                file_writer.writerow([absolute_way,label])


def main():
    folderpath='dataset_folder'
    with open("annotation_train.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator='\n')
        file_writer.writerow(
            ["folder_path", "label"])
    subdir = "zebra"
    create_annotation(subdir, '1', folderpath)
    subdir = "bayhorse"
    create_annotation(subdir, '0', folderpath)
    print("Конец")


if __name__ == "__main__":
    main()
