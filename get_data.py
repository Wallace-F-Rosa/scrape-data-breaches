import pandas as pd
import argparse
from bs4 import BeautifulSoup
import requests
import json

url = 'https://en.wikipedia.org/wiki/List_of_data_breaches'

def get_references():
    """Getting links from the 'Reference section'. BeautifulSoup is used to scrape data
    using the html tags.
        
        Return:
            references (dict) : dictionary with references in the same order found on
        the References section. First reference will have key 1, second will have key 2, etc...
    """
    references = {}
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    ol_references = soup.find('ol', class_='references')
    links = ol_references.find_all('a', class_='external text')

    i = 1
    for link in links:
        references[i] = link.get('href')
        i+=1

    return references

def get_breaches(output_file, django_model=None):
    """Getting data breaches data using pandas. Pandas allows easier manipulation
    of columns and data rows.
        Data is dumped on file named after output_file parameter.
    """
    df = pd.read_html(url, header=0)
    data = df[0]

    # drop missing values
    data = data.dropna()

    # convert records to numeric, any bad values will be NaN
    data['Records'] = pd.to_numeric(data['Records'], errors='coerce')

    # drop NaN Records
    data = data.dropna()

    # convert to integer
    data['Records'] = data['Records'].astype('int64', errors='raise')

    # rename columns
    data = data.rename(columns={
        'Entity' : 'entity',
        'Year' : 'year',
        'Records' : 'records',
        'Organization type' : 'organization_type',
        'Method' : 'method',
        'Sources' : 'sources'
    })

    # treat case of organization with more then one type (e.g. 'financial, credit reporting')
    org_type_data = []
    for index, row in data.iterrows():
        content = str(row['organization_type']).split(', ')
        org_type_data.append(content)

    data['organization_type'] = org_type_data

    # make entity an object with name and organization_type
    orgs_data = []
    for index, row in data.iterrows():
        entity_data = {
                'name' : row['entity'],
                'organization_type' : row['organization_type']
            }
        orgs_data.append(entity_data)

    data['entity'] = orgs_data

    data = data.drop(columns=['organization_type'])

    # replace references strings with urls
    references = get_references()

    refs_data = []

    for index, row in data.iterrows(): 
        content = str(row['sources']).replace('[', ' ').replace(']', ' ').split(' ')
        content = [int(c) for c in content if c != '']
        refs = []
        for c in content:
            refs.append(references[c])
        refs_data.append(refs)
        # print(refs_data)
    
    data['sources'] = refs_data

    output_json = json.loads(data.to_json(orient='records'))

    with open(output_file, 'w+', encoding='utf-8') as outf:
        json.dump(output_json, outf, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    """Main function. Sets program parameters and call scraper function.
    """

    parser = argparse.ArgumentParser(
                prog='Scraping Data Breaches from Wikipidia' 
            )
    parser.add_argument('--output', '-o', type=str, default='data.json', help='Output file of Data Breaches json data')
    args = parser.parse_args()
    get_breaches(args.output)
