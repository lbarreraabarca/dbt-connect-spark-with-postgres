import csv
import random

records=2600
print("Making %d records\n" % records)

fieldnames=['id','name','age','city']
writer = csv.DictWriter(open("people.csv", "w"), fieldnames=fieldnames)

random.randrange(5, 600) * random.random()
names=['Deepak', 'Sangeeta', 'Geetika', 'Anubhav', 'Sahil', 'Akshay', 'Joseph', 'Nicholas', 'Abraham', 'John', 'Bill', 'Louis', 'Phill', 'Maximus', 'Alan', 'Edmond', 'Walter']

#for i in range(0, records):
#    print('INSERT INTO dwh.customers VALUES (' + str(i) + ',' + "'" + random.choice(names) + "');")

for i in range(0, records):
    order = i*1000
    customer = i%300
    print('INSERT INTO dwh.orders VALUES ('+ str(order) + ',' + str(round(random.randrange(5, 600) * random.random(), 2) ) + ',' + str(customer) + ");")