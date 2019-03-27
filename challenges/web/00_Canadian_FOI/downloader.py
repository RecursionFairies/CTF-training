import requests
from tqdm import tqdm

baseurl = "http://foi.uni.hctf.fun/docs/document_"

for number in tqdm(range(0, 999)):
    pdf_number = "0"*(3-len(str(number))) + str(number)

    url = baseurl + pdf_number + ".pdf"
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open('./files/file_' + pdf_number + '.pdf', 'wb') as fd:
            for chunk in r:
                fd.write(chunk)
