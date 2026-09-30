import pandas as pd
import chromadb


class Portfolio:
    def __init__(self, file_path="portfolio.csv"):
        self.data = pd.read_csv(file_path)

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="portfolio"
        )

    def load_portfolio(self):
        if self.collection.count() == 0:

            for index, row in self.data.iterrows():
                self.collection.add(
                    documents=[
                        f"Project: {row['Project']}. "
                        f"Technologies: {row['Techstack']}"
                    ],
                   metadatas=[
    {
        "project": row["Project"],
        "techstack": row["Techstack"],
        "link": row["Links"]
    }
],
                    ids=[str(index)]
                )

    def query_links(self, skills):
        result = self.collection.query(
            query_texts=[" ".join(skills)],
            n_results=2
        )

        return result["metadatas"][0]