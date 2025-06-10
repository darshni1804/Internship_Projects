from bs4 import BeautifulSoup

def load_html(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return ""

def extract_posts(soup):
    post_elements = soup.find_all(name="div", class_="person")
    posts = []

    for post in post_elements:
        name = post.find(name="h1", class_="name")
        city = post.find(name="h2", class_="city")
        company = post.find(name="h3", class_="company")
        designation = post.find(name="p", class_="designation")

        # Use .text only if tag exists
        posts.append({
            'name': name.text.strip() if name else "N/A",
            'city': city.text.strip() if city else "N/A",
            'company': company.text.strip() if company else "N/A",
            'designation': designation.text.strip() if designation else "N/A"
        })

    return posts

# Change file name to 'Darshni.html'
html_content = load_html("Darshni.html")

if html_content:
    soup = BeautifulSoup(html_content, features="html.parser")
    posts = extract_posts(soup)

    for post in posts:
        print(f"name: {post['name']}, city: {post['city']}, company: {post['company']}, designation: {post['designation']}")
        print("----------------------------------------")
