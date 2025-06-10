from bs4 import BeautifulSoup


# Function to load HTML from file
def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# Function to extract person details
def extract_persons(soup):
    persons = []
    person_elements = soup.find_all("div", id=lambda x: x and x.startswith("person-"))

    for person in person_elements:
        name = person.find("h1").text.replace("Name: ", "").strip()
        city = person.find("h2").text.replace("City: ", "").strip()
        company = person.find("h3").text.replace("Company: ", "").strip()
        designation = person.find("p").text.replace("Designation: ", "").strip()

        persons.append({
            "name": name,
            "city": city,
            "company": company,
            "designation": designation
        })

    return persons


# Load and parse HTML
html_content = load_html("darshni.html")
soup = BeautifulSoup(html_content, "html.parser")

# Extract and print details
persons = extract_persons(soup)
for person in persons:
    print(f"Name: {person['name']}")
    print(f"City: {person['city']}")
    print(f"Company: {person['company']}")
    print(f"Designation: {person['designation']}")
    print("-" * 30)
