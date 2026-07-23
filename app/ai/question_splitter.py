import re


class QuestionSplitter:

    @staticmethod
    def split(message: str):

        text = message.strip()

        # Split by numbered questions: 1. 2. 3.
        numbered = re.split(r'\n?\s*\d+\.\s+', text)

        numbered = [q.strip() for q in numbered if q.strip()]

        if len(numbered) > 1:
            return numbered

        # Split by new lines
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        # Keep only lines that look like questions
        questions = []

        for line in lines:
            if (
                line.endswith('?')
                or line.lower().startswith((
                    'what', 'who', 'why', 'how', 'when',
                    'where', 'which', 'can', 'is', 'are',
                    'explain', 'define', 'tell', 'compare'
                ))
            ):
                questions.append(line)

        if len(questions) >= 2:
            return questions

        # Fallback: single question
        return [text]