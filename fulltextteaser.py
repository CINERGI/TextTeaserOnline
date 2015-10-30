#from __future__ import print_function
import argparse
from lxml import html
import requests
import json
from pprint import pprint

class TextTeaser:
    url = None
    title = None
    summary = None

    def __init__(self,url):
        self.url = url

# NOABSTRACT = {'None', '0'}

num_lines = sum(1 for line in open('sciencebase.json'))
print ("Number of lines in file:",num_lines )

with open('sciencebase.json') as json_file:
    data = json.load(json_file)
    #stuff = data[1]["abstractCount"]
    #pprint(stuff)
    #for line in data:
    count = 0
    urlcount = 0
    while count < num_lines:
        if data[count]["abstractCount"]:
            if data[count]["abstractCount"] != "0":
                curAbstract = data[count]["abstractCount"]
                #print('The count is:', count)
                if data[count]["otherLinks"]:
                    pprint(data[count]["otherLinks"])
                    urlcount = urlcount + 1
                    #print('urlcount is:', urlcount)
        count = count + 1

'''
def tt(inputUrl):

    with open('finaltest2.json') as data_file:
        data = json.load(data_file)
        newinputurl = data["otherlinks"]

    baseurl= 'http://www.textteaser.com/summary?url='
    inputUrl = 'http://databasin.org/datasets/57060da0c5aa4d54a8870795153996fe'
    #baseurl= 'http://www.textteaser.com/summary?url='
    #inputUrl = 'http://www.azgs.az.gov'
    #inputUrl = newinputurl
    aUrl = baseurl + inputUrl
    page = requests.get(aUrl)
    tree = html.fromstring(page.text)

    tt =  TextTeaser(inputUrl)
 # <meta property="og:title" content="Varied Thrush Future Density (mean) | Data Basin | TextTeaser" />
 #    <meta property="og:description" content="
    titleList = tree.xpath('//meta[@property="og:title"]/@content')
    if len(titleList) > 0 :
        tt.title = str(titleList[0])
    summaryList = tree.xpath('//meta[@property="og:description"]/@content')
    if (len(summaryList) > 0):
      tt.summmary = str(summaryList[0])
    return  json.dumps(tt.__dict__)

def main():
    parser = argparse.ArgumentParser(description='Parse TextTeaser Summaries.')
    parser.add_argument('-u','--url', type=str,
                   help='passs a URL to summarize')
    args = parser.parse_args()
    print tt(args.url)

if __name__ == "__main__":
    main()
'''