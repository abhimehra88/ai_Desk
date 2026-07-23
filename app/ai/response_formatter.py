class ResponseFormatter:

    # =====================================================
    # CLEAN RAW MODEL OUTPUT
    # =====================================================

    @staticmethod
    def clean(text: str) -> str:

        if not text:
            return "I couldn't generate a response right now."

        # Remove common AI fluff
        unwanted = [
            "As an AI language model,",
            "As an AI,",
            "I do not have personal opinions,",
            "I don't have feelings,",
            "Alright then",
            "Let's dive into",
            "Pocket Guide"
        ]

        for phrase in unwanted:
            text = text.replace(phrase, "")

        # Remove excessive blank lines
        lines = [line.rstrip() for line in text.splitlines()]

        cleaned = []
        prev_empty = False

        for line in lines:

            is_empty = line.strip() == ""

            if is_empty and prev_empty:
                continue

            cleaned.append(line)
            prev_empty = is_empty

        text = "\n".join(cleaned).strip()

        # Default safety limit
        max_length = 2200

        # Deep lesson can be longer
        if "###" in text or "Practice Questions" in text:
            max_length = 5000

        if len(text) > max_length:
            text = text[:2200] + "\n\n[Answer shortened]"

        return text

    # =====================================================
    # DETECT REQUEST TYPE
    # =====================================================

    @staticmethod
    def detect_request_type(question: str) -> str:

        q = question.lower()

        # Full course request
        deep_teach_keywords = [
            "from scratch",
            "complete guide",
            "full explanation",
            "10 examples",
            "step by step"
        ]

        if any(k in q for k in deep_teach_keywords):
            return "teach_deep"

        # Medium teaching
        if "teach me" in q or "teach" in q:
            return "teach_medium"

        # Cmparision
        compare_keywords = [
            "compare",
            "difference between",
            "vs",
            "better than"
        ]

        if any(k in q for k in compare_keywords):
            return "comparison"

        # Short definition
        definition_keywords = [
            "what is",
            "define",
            "meaning of"
        ]
        if any(k in q for k in definition_keywords) and len(q.split()) <= 8:
            return "definition"

        return "normal"

    # =====================================================
    # BUILD MODEL INSTRUCTION
    # =====================================================

    @staticmethod
    def build_instruction(question: str) -> str:

        request_type = ResponseFormatter.detect_request_type(question)

        # -----------------------------
        # MEDIUM TEACHING
        # -----------------------------
        if request_type == "teach_medium":
            return """
Answer as a structured mini-lesson.

Use this order:
1. One-line definition
2. One simple Java example
3. Explain each line briefly
4. One real use-case
5. One interview tip

Keep formatting clean with headings and bullet points.
Avoid long paragraphs and unnecessary stories.
"""

        # -----------------------------
        # DEEP TEACHING
        # -----------------------------
        if request_type == "teach_deep":
            return """
Answer as a structured mini-lesson.

Use this exact order:
- One-line definition
- Syntax
- Why it is used
- Step-by-step explanation
- Multiple small examples (2-4 lines each)
- 3 practice questions
- One interview/exam summary line
- Keep paragraphs under 3 lines.
- Use headings frequently.
- Prefer bullet points over long explanations.
- Put code examples in separate blocks.
- Make the answer easy to skim on a laptop screen.

Keep formatting clean with headings and bullet points.
Avoid long paragraphs and unnecessary stories.
"""

        # -----------------------------
        # SHORT DEFINITION
        # -----------------------------
        if request_type == "definition":
            return """
Answer in this format:
- Definition (1-2 lines)
- Tiny Java example if relevant
- One key exam point

Keep the total answer under 8 lines.
"""

        # -----------------------------
        # COMPARISON
        # -----------------------------
        if request_type == "comparison":
            return """
Answer using a table with:
- Feature
- Item A
- Item B

Then give a one-line conclusion.
"""

        # -----------------------------
        # DEFAULT
        # -----------------------------
        return """
Answer clearly and concisely in simple Hindi-English mix.
Use examples only if they improve understanding.
Avoid unnecessary verbosity.
"""

    # =====================================================
    # FINAL HUMAN-FRIENDLY POST PROCESSING
    # =====================================================

    @staticmethod
    def make_human(question: str, answer: str) -> str:

        q = question.lower()

        # -----------------------------
        # Coding / DSA enhancement
        # -----------------------------
        coding_keywords = [
            "java", "python", "dsa", "array", "linked list",
            "stack", "queue", "tree", "graph", "algorithm",
            "method", "class", "object", "recursion"
        ]

        if any(k in q for k in coding_keywords):

            # Encourage practical learning
            if len(answer) < 120:
                answer += (
                    "\n\nKey point: Interview me definition + small example + one use-case yaad rakhna kaafi hota hai."
                )

        # -----------------------------
        # News / live info
        # -----------------------------
        news_keywords = [
            "latest", "current", "today", "news", "winner",
            "score", "result", "fifa", "bitcoin", "price",
            "weather", "stock", "cricket"
        ]

        if any(k in q for k in news_keywords):

            if "Source:" not in answer and "Sources:" not in answer:
                answer += "\n\nSource: live web search"

        # -----------------------------
        # Emotional / personal questions
        # -----------------------------
        emotional_keywords = [
            "attached", "relationship", "love", "breakup",
            "anxiety", "overthinking", "lonely", "sad"
        ]

        if any(k in q for k in emotional_keywords):

            # Make tone warmer
            if not answer.startswith("I understand"):
                answer = "I understand why you're asking this.\n\n" + answer

        # Split very long teaching answers
        if len(answer) > 3500 and any(k in q for k in ["teach", "example", "from scratch"]):

            cut_point = answer.find("6.")

            if cut_point != -1:
                answer = (
                    answer[:cut_point]
                    + "\n\nType **continue** to see examples 6-10 and practice questions."
                )

        return answer.strip()