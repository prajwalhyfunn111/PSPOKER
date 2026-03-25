import codecs

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# fix spaces in doctype and comments that the parser may have ingested
text = text.replace("< !DOCTYPE", "<!DOCTYPE")
text = text.replace("< !--", "<!--")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
