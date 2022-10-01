# randomly extract station pairs from csv
# import metrics_extractor as me 
import Python.metrics_extractor as me 
import random 
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

