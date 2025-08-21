import os

faq_path = os.path.join(os.path.dirname(__file__), "data/faq.txt")
print("Caminho completo do FAQ:", faq_path)
print("Existe?", os.path.exists(faq_path))

with open(faq_path, "r", encoding="utf-8") as f:
    for line in f:
        print(repr(line))