import os
import requests

from pathlib import Path

import pdfplumber

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

filename = Path('metadata.pdf')

url = 'https://kkm.salyk.kg/kkm/check?rnmNumber=4868&checkNumber=24177&amount=120.00&date=2022-06-02_10:17:19'
response = requests.get(url)

filename.write_bytes(response.content)

with pdfplumber.open('metadata.pdf') as pdf:
    
    for i in range(len(pdf.pages)):
        data = pdf.pages[i].extract_text()
        
        with open('data.txt', 'w') as f:
            f.write(data)
        

file_path = 'metadata.pdf'

if os.path.isfile(file_path):
    os.remove(file_path)

with open("data.txt", 'r') as f:
    
    with open('info.txt', 'w') as a:
        
        for line in f:
            search_word =  ["ИНН","Всего", "№"]
            
            for i in search_word:
                
                if i in line:
                    a.write(line)
                    
                    for i in line.split():
                        if is_number(i):
                            print(i)


