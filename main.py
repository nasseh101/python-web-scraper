import requests
from bs4 import BeautifulSoup
from csv import writer
import csv

with open ('csv/all-scrape-2019-10-17-hour-12.csv') as csv_file_in:
    csv_reader = csv.reader(csv_file_in, delimiter=',')
    line_count = 0

    with open('output/all-scrape-new.csv', 'w') as csv_file_out:
        csv_writer = writer(csv_file_out)
        headers = ['category', 'date', 'rank', 'name', 'appID', 'totalReviews', 'aggReviews', 'description']
        csv_writer.writerow(headers)

        for row in csv_reader:
            if line_count == 0:
                line_count += 1

            else:
                response = requests.get(row[4])
                soup = BeautifulSoup(response.text, 'html.parser')
                rawDescription = soup.find(class_='ui-expandable-content__inner')

                if rawDescription is not None:
                    description = rawDescription.get_text().replace('\n', ' ')
                    qMarkLocation = row[4].find('?')
                    text = row[4]
                    appID = text[25:qMarkLocation]
                    csv_writer.writerow([row[0],row[1],row[2],row[3],appID,row[5],row[6],description])

                line_count += 1

    print ("\nFinished Scrape")

