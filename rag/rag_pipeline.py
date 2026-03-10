from groq import Groq
import json

class RAGPipeline:

    def __init__(self, vector_store, embedding_model, api_key):
        self.vector_store = vector_store
        self.embedding_model = embedding_model
        self.client = Groq(api_key=api_key)

    def generate_summary(self, query):
        query_vec = self.embedding_model.embed(query)
        docs = self.vector_store.search(query_vec)

        structured_events = []
        for d in docs:
            try:
                structured_events.append(json.loads(d))
            except:
                pass

        context = json.dumps(structured_events, indent=2)

        prompt = f"""
You are an AI system assisting police patrol operations.

You will receive structured event data in JSON.

STRICT RULES:
- Use ONLY the numbers present in the JSON.
- Do NOT estimate or invent numbers.
- If a value is missing, say "not detected".
- Treat backpacks and suitcases as unattended bag risks.
- Ignore normal items like plants.

Event Data:
{context}

Query:
{query}

Generate a patrol intelligence summary including:

1. Crowd situation
2. Vehicle activity
3. Security risks
4. Patrol recommendation

Limit to 100 words.
"""

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1
        )

        return response.choices[0].message.content
