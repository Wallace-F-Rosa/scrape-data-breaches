# Data breaches scraper
This scraper gets data from [Wikipidia's List of Data Breaches](https://en.wikipedia.org/wiki/List_of_data_breaches) and returns a json list containing the data of all databreaches. Built using Python, pandas and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#).

Each data breach contains:

| field | description |
| ----- | ----------- |
| entity | object containing name of the organization and organization_type(sphere of activity) |
| year | Integer representing wich year the breach occurred. |
| method | string containing the method used in the breaching process. |
| sources | List of strings containing the urls of midia sources covering the data breach. |

## Requirements 
Required python packages:
* pandas
* lxml 
* beautifulsoup4
* requests

## Installation and use
Install the requirements with `pip`:

`pip install -r requirements.txt`

Run the program with python :

`python get_data.py`

The data will be in the `data.json` file.

## Other options
Program options available : 

```
usage: Scraping Data Breaches from Wikipidia [-h] [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output file of Data Breaches json data.
```
