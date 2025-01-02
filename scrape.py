import requests
from bs4 import BeautifulSoup

url = "https://en.wikivoyage.org/wiki/Purnululu_National_Park"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
content_div = soup.find(id="mw-content-text")
content_paragraphs = content_div.find_all("p")

article_history_link = "https://en.wikivoyage.org/w/index.php?title=Purnululu_National_Park&action=history"
article_name = "Purnululu National Park"
article_name_short = "Purnululu"

notice = "<p><i>This content is copied from the " + \
 "<a href=\"" + url + "\" target=\"_blank\" rel=\"noopener noreferrer\">" + article_name + "</a> article on Wikivoyage, which is licensed under" + \
 " <a href=\"https://creativecommons.org/licenses/by-sa/4.0/\" target=\"_blank\" rel=\"noopener noreferrer\">Creative Commons Attribution-ShareAlike 4.0 International License</a>. That article is also based on work licensed under" + \
 " <a href=\"https://creativecommons.org/licenses/by-sa/3.0/\" target=\"_blank\" rel=\"noopener noreferrer\">Creative Commons Attribution-ShareAlike 3.0 License</a> from other websites. Details of contributors to that article can be found in the" + \
 " <a href=\"" + article_history_link + "\" target=\"_blank\" rel=\"noopener\">article history</a>.</i></p>" + \
 "<p><i>This page and everything in the <a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://github.com/darkmodetest/darkmodetest.github.io\">GitHub repo</a> is licensed under the <a href=\"https://creativecommons.org/licenses/by-sa/4.0/\" target=\"_blank\" rel=\"noopener noreferrer\">Creative Commons Attribution-ShareAlike 4.0 International License</a></i></p>"


block = ""
total_words = 0
blocks = []
for paragraph in content_paragraphs:
    words = paragraph.text
    total_words += len(words.split())
    block += "<p>" + paragraph.text + "</p>\n"
    if total_words >= 500:
        blocks.append(block)
        block = ""
        total_words = 0

i = 0
for block in blocks:
    i += 1
    with open(f'{article_name_short.lower()}{i}.html', 'w') as f:
        f.write("<!DOCTYPE html>" + \
        "<html lang=\"en\">" + \
        "<head>" + \
		"<meta charset=\"utf-8\">" + \
		"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">" + \
		f"<title>Dark Mode Readability Test: {article_name_short} {i}</title>" + \
		"<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" />" + \
		"</head>" + \
		"<body>" + \
		"<main>")
        f.write(f"<h1>Dark Mode Readability Test: {article_name_short} {i}</h1>")
        f.write(notice)
        f.write(block)

        f.write("</main>" + \
            "</body>" + \
            "</html>")
