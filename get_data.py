import pandas as pd

def get_breaches():
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
    data.to_json('data.json', orient='records')

if __name__ == '__main__':
    get_breaches()
