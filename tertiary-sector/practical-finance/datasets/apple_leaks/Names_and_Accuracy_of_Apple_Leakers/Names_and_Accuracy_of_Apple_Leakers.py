import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://appletrack.com/leaderboard/"
page = requests.get(URL).text
doc = BeautifulSoup(page, "html.parser")
with open("test.html", "w") as test_html_file:
    test_html_file.write(str(doc))
rows = doc.find(class_="wp-block-table is-style-regular").find("table").find("tbody").find_all("tr")
name_and_accuracy = {
    "Names": [],
    "Accuracy": [],
}
for row in rows:
    row = row.find_all("td")
    name = row[1].text
    accuracy = row[2].text
    name_and_accuracy["Names"].append(name)
    name_and_accuracy["Accuracy"].append(accuracy)
names_and_accuracy = pd.DataFrame(name_and_accuracy)
names_and_accuracy.to_csv("./Names_and_Accuracy_of_Apple_Leakers.csv", index=False)
names_and_accuracy.to_json("./Names_and_Accuracy_of_Apple_Leakers.json")
names_and_accuracy.to_excel("./Names_and_Accuracy_of_Apple_Leakers.xlsx")
