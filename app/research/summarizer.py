class SearchSummarizer:

    @staticmethod
    def build_context(search_data):

        if not search_data.get("success"):
            return None

        query = search_data.get("query", "")
        results = search_data.get("results", [])

        if not results:
            return None

        context = f"User searched for: {query}\n\n"
        context += "Live web search results:\n\n"

        for i, item in enumerate(results, start=1):

            title = item.get("title", "")
            snippet = item.get("snippet", "")

            context += f"{i}. {title}\n"
            context += f"Snippet: {snippet}\n\n"

        # Final instruction for Gemini
        context += (
            "Using these live web results, answer the user's question.\n\n"

            "CRITICAL RULES:\n"
            "- Treat the web search results as the primary source of truth.\n"
            "- If the web results are more recent than your built-in knowledge, trust the web results.\n"
            "- Do not override recent web evidence with older model memory.\n"
            "- Prefer official sources (FIFA) and major news organizations (Reuters, AP, BBC, etc.).\n"
            "- If sources disagree, explicitly mention the disagreement.\n"
            "- If the results confirm a winner, report the winner and cite that it is based on live web search results.\n"
            "- Never say an event has not happened if recent web results indicate that it has occurred.\n"
        )

        return context