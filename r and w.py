'''
# write and read
fw = open('text.txt','w')
fw.write('writing some stuff in my file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('text.txt','r')
text = fr.read()
print(text+'fuck you')
'''

# web download read and split
from urllib import request
url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
def download_data(durl):
    res = request.urlopen(durl)
    download = res.read()
    download_str = str(download)
    lines = download_str.split(" ")
    dest_url = r"goog.csv"
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line+"\n")
    fx.close()
download_data(url)