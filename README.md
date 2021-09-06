# Data breaches scraper
This scraper gets data from [Wikipidia's List of Data Breaches](https://en.wikipedia.org/wiki/List_of_data_breaches) and returns a json list containing the data of all databreaches. Built using Python and pandas.

Each data breach contains:

| field | description |
| ----- | ----------- |
| entity | A string with the name of the entity that suffered the breach. |
| year | Integer representing wich year the breach occurred. |
| organization_type | String representing the entity's sphere of activity. |
| method | List of strings containing the methods used in the breaching process. |
| sources | List of strings containing the urls of midia sources covering the data breach. |

## Requirements 
Required python packages:
* pandas
* lxml 

## Installation and use
Install the requirements with `pip`:

`pip install -r requirements.txt`

Run the program with python :

`python get_data.py`

The data will be in the `data.json` file.

## Other options
Program options available : 

```
usage: Scraping Data Breaches from Wikipidia [-h] [--output OUTPUT] [--django-model-name DJANGO_MODEL_NAME]

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output file of Data Breaches json data.
  --django-model-name DJANGO_MODEL_NAME, -d DJANGO_MODEL_NAME
                        Export data as Django fixture informing the Model name.
```
