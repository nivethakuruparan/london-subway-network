import Python.metrics_extractor as me
import random 
# import metrics_extractor as me


#randomly chooses n connected station pairs to test, where n is the ith index in dictionary kpi_data
def generate_kpi_data():
    kpi_data = {
        10 : [],
        20 : [],
        50 : [],
        100 : [],
        200 : [],
        300 : [],
        400 : [] 
    }   
    conn_pairs = me.extract_connection_pairs('_dataset/london.connections.csv')
    conn_range = len(conn_pairs)-1
    for i in kpi_data:
        count = 0
        while count< i:
            ind = random.randint(0, conn_range)
            kpi_data[i].append(conn_pairs[ind])
            count += 1
    return kpi_data

def generate_time_data(gr):
    deg_list = []
    for i in gr.values():
        deg_list.append((len(i.neighbours)))
    min_degree = min(deg_list)
    max_degree = max(deg_list)
    time_data = {}
    for i in range(min_degree, (max_degree+1)):
        time_data.update({i: None})

    for i in gr.values():
        deg = len(i.neighbours)
        if (time_data[deg] == None):
            ind = random.randint(0, deg-1)
            time_data[deg] = [i.id, i.neighbours[ind][0]]

    time_data = {key:val for key,val in time_data.items() if val!=None}
    return time_data