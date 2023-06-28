import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import desc

URL = "https://appletrack.com/leaderboard/"
page = requests.get(URL).text
doc = BeautifulSoup(page, "html.parser")
with open("test.html", "w") as test_html_file:
    test_html_file.write(str(doc))
rows = doc.find(class_="wp-block-table is-style-regular").find("table").find("tbody").find_all("tr")
data = {
    "Name": [],
    "Accuracy": [],
    "Link of Leaker Dashboard": [],
    "Description": [],
    "Img": [],
    "Status": [],
    "Leak": [],
    "Leak Link": [],
}
for row in rows:
    row = row.find_all("td")
    name = row[1].text
    accuracy = row[2].text
    link = row[1].find("a").attrs["href"]
    URL = link
    page = requests.get(URL).text
    doc = BeautifulSoup(page, "html.parser")
    description = doc.find("div", class_="entry-content").find("p")
    try:
        url = description.find("a").attrs["href"]
    except:
        url = None
    description = description.text
    img = (
        doc.find(
            "div",
            class_="single-title-zone-classic we mx-auto col",
        )
        .find("img")
        .attrs["src"]
    )
    tables = doc.find_all(class_="wp-block-table")
    for table in tables:
        rows = table.find("table").find("tbody").find_all("tr")
        for row in rows:
            row = row.find_all("td")
            status = row[0].text
            leak = row[1].text
            try:
                leak_link = row[1].find("a").attrs["href"]
            except:
                leak_link = None
            data["Name"].append(name)
            data["Accuracy"].append(accuracy)
            data["Link of Leaker Dashboard"].append(URL)
            data["Description"].append(description)
            data["Img"].append(img)
            data["Status"].append(status)
            data["Leak"].append(leak)
            data["Leak Link"].append(leak_link)
Each_Leak = pd.DataFrame(data)
Each_Leak.to_csv("./Each_Leak.csv", index=False)
Each_Leak.to_json("./Each_Leak.json")
Each_Leak.to_excel("./Each_Leak.xlsx")

