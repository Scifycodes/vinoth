from scholarly import scholarly
import json

AUTHOR_ID = "3DH2k5cAAAAJ"

author = scholarly.search_author_id(AUTHOR_ID)
author = scholarly.fill(author)

publications = []

for pub in author["publications"]:
    pub_filled = scholarly.fill(pub)
    bib = pub_filled["bib"]

    publications.append({
        "title": bib.get("title", ""),
        "authors": bib.get("author", ""),
        "year": bib.get("pub_year", ""),
        "journal": bib.get("journal", ""),
        "url": pub_filled.get("pub_url", "")
    })

with open("publications.json", "w", encoding="utf-8") as f:
    json.dump(publications, f, indent=2, ensure_ascii=False)

print("Publications imported successfully!")


# import json

with open("publications.json", "r", encoding="utf-8") as f:
    publications = json.load(f)

html = "<ul class='publications'>\n"

for p in publications:
    html += "  <li>\n"
    html += f"    <strong>{p['title']}</strong><br>\n"
    html += f"    {p['authors']} ({p['year']})<br>\n"
    html += f"    <em>{p['journal']}</em><br>\n"
    if p["url"]:
        html += f"    <a href='{p['url']}'>Paper link</a>\n"
    html += "  </li>\n"

html += "</ul>"

with open("publications.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Website publications updated!")
