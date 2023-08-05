import csv

filename ='group.csv'

id_name='ID'

d={}

title = [id_name]

with open(filename, encoding='utf-8') as file,\
     open('condensed.csv', 'w', newline='') as out:
     
    for i in csv.reader(file):
        d.setdefault(i[0], {}).update({i[1]: i[2]})
        if i[1] not in title:
            title.append(i[1])
    print(d.items())        
    writer = csv.writer(out)
    writer.writerow(title)
    [writer.writerow([i, *d[i].values()]) for i in d]