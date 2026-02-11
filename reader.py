import csv


def reader_csv_file(file_path):
    list_file=[]
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            list_file.append(row)
    return list_file

file_path='network_traffic.log'
data=reader_csv_file(file_path)
# for row in data:
#     print(row)

def external_ip(data):
    external_ip_list = []
    for row in data:
        ip=row[1]
        if not ip.startswith('192') and not ip.startswith('10.'):
            external_ip_list.append(row)
    return external_ip_list

# external_ip_list=external_ip(data)
# for row in external_ip_list[ :50]:
#     print(row)





def sensitive_port(data):
    sensitive_port_lst = []
    for row in data:
        port = row[3]
        if port=='22' or port=='23' or port=='3389':
            sensitive_port_lst.append(row)
    return sensitive_port_lst

sensitive_port_list=sensitive_port(data)
for row in sensitive_port_list:
    print(row)


