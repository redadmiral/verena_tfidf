import json
from src.index import Index, Article

index = Index()

articles_raw = []
with open("data/cleaned.jsonl") as f:
    for row in f:
        a = json.loads(row)
        index.add(Article(title=a['title'], text=a['text'], source=a['shareUrl']))

query = "Volker Heißmann Fasching Orden"

print(json.dumps(index.search(query, limit=5), indent=4, ensure_ascii=False))
