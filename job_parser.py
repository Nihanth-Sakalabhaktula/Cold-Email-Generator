import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0
)

def extract_job_details(job_description):
    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert job description analyzer.

        Extract the following information from the job description:
        - role
        - experience
        - skills
        - description

        Return ONLY valid JSON in this format:

        {{
            "role": "",
            "experience": "",
            "skills": [],
            "description": ""
        }}

        Job Description:
        {job_description}
        """
    )

    chain = prompt | llm

    response = chain.invoke({
        "job_description": job_description
    })

    content = response.content.strip()

    # Remove Markdown formatting if the model returns ```json ... ```
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)