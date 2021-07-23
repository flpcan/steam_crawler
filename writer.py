import csv

def write(name,price):
    with open('csdata.csv','a', newline='\n') as f:

        csv_writer = csv.writer(f)

        csv_writer.writerow([f"{name}",f"{price}"])
        # csv_writer.writerow(['tom','hanks','tom@gmail.com'])
        f.close()


# csv_writer.writerow(['tom','hanks','tom@gmail.com'])



# reader()
