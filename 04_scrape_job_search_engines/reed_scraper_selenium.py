import csv
import math
import time
from utils import connect_to_page_with_selenium, extraction_from_listing_page

if __name__ == "__main__":
    start_time = time.time()
    job_name = input("What kind of job are you looking for?") or "software-developer"
    job_city = input("Which city would you like to work in?") or "london"
    print("Thank you for your answers! ..creating a csv document for you")

    csv_name = "{0}_{1}.csv".format(job_name, job_city)
    with open(csv_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["title", "id", "salary", "type", "location", "description", "skills", "is_remote"])

        url = "https://www.reed.co.uk/jobs/{0}-jobs-in-{1}".format(job_name, job_city)
        soup = connect_to_page_with_selenium(url)
        extraction_from_listing_page(writer, soup)

        page_counter = soup.find("div", {"class": "page-counter"}).text
        limit = input("How much page do you want to scrape?") \
                or math.ceil(int(page_counter.split("of ")[1].split(" jobs")[0].replace(",", ""))/25)
        for page_number in range(2, int(limit)+1):
            next_url = url + "?pageno={0}".format(page_number)
            soup = connect_to_page_with_selenium(next_url)
            extraction_from_listing_page(writer, soup)
            print("scraped {0} pages".format(page_number))
    print("The execution time was: --- %s seconds ---" % (time.time() - start_time))
    print("finished! You can read the best available positions in the document {0}".format(csv_name))

### The execution time was: --- 257.2125859260559 seconds ---
