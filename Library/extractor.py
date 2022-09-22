import csv


def extract_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = list(reader)

    return data


# def read_input(file_path):
#     file = open(file_path, 'r')  # opening file in read mode
#     file.readline()  # skipping the first line

#     lines = file.readlines()  # iterating through the lines
#     file_list = [] #list of tuples, each tuple is an entry in the file 

#     for line in lines:
#         full_list = tuple(line.strip().split(','))
#         file_list.append(full_list)

#     return file_list

# def read_input():
#     file1 = open('../_dataset/london.connections.csv', 'r')  # opening file in read mode
#     file1.readline()  # skipping the first line

#     file2 = open('../_dataset/london.lines.csv', 'r')
#     file2.readline()

#     file3 = open('../_dataset/london.stations.csv','r')
#     file3.readline()


#     lines1 = file1.readlines()  # iterating through the lines
#     connections_list = [] #list of tuples, each tuple is an entry in the file 

#     for line in lines1:
#         full_list = tuple(line.strip().split(','))
#         connections_list.append((int(full_list[0]), int(full_list[1]), int(full_list[2]), int(full_list[3])))


#     lines2 = file2.readlines()
#     lines_list = []

#     for line in lines2:
#         full_list = tuple(line.strip().split(','))
#         lines_list.append((int(full_list[0]), full_list[1], full_list[2], full_list[3]))

#     return connections_list, lines_list


    

    # lines3 = file3.readlines()
    # stations_list = []
    
    # for line in lines3:
    #     if not line.strip():
    #     full_list = tuple(line.strip().split(','))
    #     print("now on")
    #     print(full_list[0])
    #     stations_list.append((int(full_list[0]), full_list[1], full_list[2], full_list[3], full_list[4]))
    #     else:
    #          continue 

    

