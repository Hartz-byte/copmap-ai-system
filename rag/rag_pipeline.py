from groq import Groq

class RAGPipeline:

    def __init__(self, vector_store, embedding_model, api_key):
        self.vector_store = vector_store
        self.embedding_model = embedding_model
        self.client = Groq(api_key=api_key)

    def generate_summary(self, query):
        query_vec = self.embedding_model.embed(query)
        docs = self.vector_store.search(query_vec)
        context = "\n".join(docs)

        prompt = f"""
        Context:
        {context}

        Query:
        {query}

        You are an AI assistant helping police patrol analysis.

        Use ONLY the provided event data.

        Do NOT invent numbers or objects.

        Classify risk using:
        - Crowd density
        - Vehicle activity
        - Suspicious objects (weapons, unattended bags)

        Ignore normal objects like plants or handbags.

        Provide:

        1. Crowd summary
        2. Traffic activity
        3. Security risks
        4. Patrol recommendation

        Keep the summary under 120 words.
        """

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content
