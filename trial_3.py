#import print_function

import argparse
import json
import os

import requests
import json
#from newspaper import Article
import csv



from rosette.api import API, DocumentParameters, RosetteException


def start(key, name,alt_url ='https://api.rosette.com/rest/v1/' ):
    #get page
    url_1="https://api.gdeltproject.org/api/v2/doc/doc?query=domain:"
    url_2="&sourcelang:english&maxrecords=250&format=json&startdatetime=20180607000000&enddatetime=20180612000000"
    response = requests.get(url_1+name+url_2)
    data = response.json()
    
    
    articles = data['articles']
    
    with open(name+"_data.txt", mode='wb') as outfile:
        
        for i in articles:
        #        i = articles[0]
            link = i['url']
            categories_url_data = link
            url = categories_url_data
            
            data = run(key,url,alt_url)
            if data!=None:
                json.dump(data, outfile)
                outfile.write("\n")
        outfile.close()
    


def run(key,url, alt_url='https://api.rosette.com/rest/v1/'):
    """ Run the example """
    
    
    # Create an API instance
    api = API(user_key=key, service_url=alt_url)
    params = DocumentParameters()

    # Use a URL to input data instead of a string
    params["contentUri"] = url
    try:
        return(api.sentiment(params))
    except RosetteException as exception:
        print(exception)
        return None


PARSER = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 description='Calls the ' +
                                 os.path.splitext(os.path.basename(__file__))[0] + ' endpoint')
PARSER.add_argument('-k', '--key', help='Rosette API Key', required=True)
PARSER.add_argument('-u', '--url', help="Alternative API URL",
                    default='https://api.rosette.com/rest/v1/')
PARSER.add_argument('-n', '--name', help="Website Name")

if __name__ == '__main__':
    ARGS = PARSER.parse_args()
    RESULT = start(ARGS.key, ARGS.name,ARGS.url)
    print(json.dumps(RESULT, indent=2, ensure_ascii=False, sort_keys=True).encode("utf8"))
