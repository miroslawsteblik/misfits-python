# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:50:00 2023

@author: miros
"""


import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

"""
We first initialize a requests session, we use the User-Agent header to indicate that 
we are just a regular browser and not a bot (some websites block them), and then we get the 
HTML content using session.get() method. After that, we construct a BeautifulSoup object using html.parser.
"""
def get_soup(url):
    """Constructs and returns a soup using the HTML content of `url` passed"""
    # initialize a session
    session = requests.Session()
    # set the User-Agent as a regular browser
    session.headers['User-Agent'] = USER_AGENT
    # request for english content (optional)
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    # make the request
    html = session.get(url)
    # return the soup
    return bs(html.content, "html.parser")

def get_all_tables(soup):
    """Extracts and returns all tables in a soup object"""
    return soup.find_all("table")

def get_table_headers(table):
    """Given a table soup, returns all the headers"""
    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())
    return headers

"""
All the below function is doing, is to find tr tags (table rows) and extract td elements
 which then appends them to a list. The reason we used table.find_all("tr")[1:] and not all tr tags,
 is because the first tr tag corresponds to the table headers; we don't wanna add it here.
"""

def get_table_rows(table):
    """Given a table, returns all its rows"""
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        if len(tds) == 0:
            # if no td tags, search for th tags
            # can be found especially in wikipedia tables below the table
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            # use regular td tags
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows

def save_as_csv(table_name, headers, rows):
    # Check if the number of columns matches the number of headers
    if len(headers) != len(rows[0]):
        raise ValueError("Number of headers does not match the number of columns in the data")

    # Create DataFrame and save as CSV
    pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv", index=False)

"""
- Parsing the HTML content of the web page given its URL by constructing the BeautifulSoup object.
- Finding all the tables on that HTML page.
- Iterating over all these extracted tables and saving them one by one.
"""
  
def main(url):
    # get the soup
    soup = get_soup(url)
    # extract all the tables from the web page
    tables = get_all_tables(soup)
    print(f"[+] Found a total of {len(tables)} tables.")
    # iterate over all tables
    for i, table in enumerate(tables, start=1):
        # get the table headers
        headers = get_table_headers(table)
        # get all the rows of the table
        rows = get_table_rows(table)
        # save table as csv file
        table_name = f"table{i}"
        print(f"[+] Saving {table_name}")
        save_as_csv(table_name, headers, rows)

# if __name__ == "__main__":
#     import sys
#     try:
#         url = sys.argv[1]
#     except IndexError:
#         print("Please specify a URL.\nUsage: python_html_table_extractor.py [URL]")
#         exit(1)
#     main(url)
        
url = "https://www.w3schools.com/html/html_tables.asp"

main(url)