"""
Your task is to blacklist (print) a list of IP addresses.
file a.txt contains a list of country codes and IDs
file b.txt contains the same IDs and the IPs in question
file c.txt contains a list of country codes that need to be blacklisted

a.txt = 112233 US
        223344 GB
        334455 IT
        445566 AU

b.txt = 112233 127.0.0.1/32
        112233 127.0.0.2/32
        223344 721.0.0.0/32
        334455 345.0.0.0/32
        445566 456.0.0.0/32

c.txt = GB
        IT
"""

with open('a.txt', 'r') as f:
    a = [i.strip().split() for i in f.readlines()]

with open('b.txt', 'r') as f:
    b = [i.strip().split() for i in f.readlines()]

with open('c.txt', 'r') as f:
    c = [i.strip() for i in f.readlines()]

data = []
for i in a:
    stats = {}
    stats['id'] = i[0]
    stats['cc'] = i[1]
    data.append(stats)

a_data = data

data = []
for i in b:
    stats = {}
    stats['id'] = i[0]
    stats['ip'] = i[1]
    data.append(stats)

b_data = data


for x in a_data:
    for y in b_data:
        if x['cc'] in c:
            if x['id'] == y['id']:
                print y['ip']

