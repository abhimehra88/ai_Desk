from app.research.web_search import WebSearch

result = WebSearch.search("latest FIFA World Cup news")

print("Success:", result["success"])
print("Query:", result["query"])
print()

for i, item in enumerate(result["results"], start=1):
    print(f"{i}. {item['title']}")
    print(f"   {item['link']}")
    print(f"   {item['snippet'][:120]}")
    print()