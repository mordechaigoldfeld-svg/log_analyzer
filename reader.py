import csv

def reader_csv_file(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        return [row for row in csv_reader]

file_path='network_traffic.log'
data=reader_csv_file(file_path)
# for row in data:
#     print(row)



def external_ip(data):
    return[row for row in data
        if not row[1].startswith('192') and not row[1].startswith('10.')
    ]

# external_ip_list=external_ip(data)
# for row in external_ip_list[ :50]:
#     print(row)

def sensitive_port(data):
    return[row
           for row in data
           if row[3]=='22' or row[3]=='23' or row[3]=='3389'
           ]


# sensitive_port_list=sensitive_port(data)
# for row in sensitive_port_list:
#     print(row)


def big_size(data):
    return[row
           for row in data
           if int(row[5]) >5000]
# big_bite=big_size(data)
# for row in big_bite[:50]:
#     print(row)

def size_status(data):
    return[row+['large']  if int(row[5]) > 5000 else row+['normal']
           for row in data]

size_update=size_status(data)
for row in size_update:
    print(row)

