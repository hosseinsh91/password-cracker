from hashlib import sha256
import csv
def hash_password_hack(input_file_name, output_file_name):
    f=open(input_file_name)
    g=open(output_file_name , 'w')
    reader=csv.reader(f)
    writer=csv.writer(g)
    for row in reader:
        name=row[0]
        for i in range (1000 , 10000):
            n=str(i)
            hashed=sha256(n.encode('utf-8'))
            code_hashed = hashed.hexdigest()
            if code_hashed==row[1]:
                answer=(name , n)
                writer.writerow(answer)
