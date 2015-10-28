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

# NOABSTRACT = {'None', '0', 'Null'}

with open('sciencebase.json') as json_file:
    data = json.load(json_file)
    #stuff = data[1]["abstractCount"]
    #pprint(stuff)

    #current having issues where it does not find the null objects
    count = 0
    while (count < 5):
        curAbstract = data[count]["abstractCount"]
        if curAbstract is None:
            pprint('----------')
            print('The count is:', count)
            pprint(data[count]["abstractCount"])
            #pprint(data[count]["otherLinks"])
            count = count + 1
        else:
            break

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