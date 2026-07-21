from app.research.web_search import WebSearch
from app.research.summarizer import SearchSummarizer

search_data = WebSearch.search("latest FIFA World Cup news")

context = SearchSummarizer.build_context(search_data)

print(context)
