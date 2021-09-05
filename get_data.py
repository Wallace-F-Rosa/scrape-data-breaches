import pandas as pd
import argparse


def get_breaches(output_file, django_model=None):
    url = 'https://en.wikipedia.org/wiki/List_of_data_breaches'
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
        'Organization Type' : 'organization_type',
        'Method' : 'methods',
        'Sources' : 'sources'
    })
    data.to_json(output_file, orient='records')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                prog='Scraping Data Breaches from Wikipidia' 
            )
    parser.add_argument('--output', '-o', type=str, default='data.json', help='Output file of Data Breaches json data')
    parser.add_argument('--django-model-name', '-d', type=str, action='store', help='Export data as Django fixture informing the Model name')
    args = parser.parse_args()
    get_breaches(args.output, args.django_model_name)
