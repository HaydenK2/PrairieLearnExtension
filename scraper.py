from bs4 import BeautifulSoup

def webScrape():
    page = open("test.html", "r")

    soup = BeautifulSoup(page, "html.parser")

    results = soup.find(id="ResultsContainer")

    job_elements = results.find_all("div", class_="card-content")
    dict = []

    for job_element in job_elements:
        title = job_element.find("h2", class_="title").text.strip()
        date = job_element.find("time").text.strip()
        d = {"title" : title, "date" : date}
        dict.append(d)

    print(dict)

    return dict

