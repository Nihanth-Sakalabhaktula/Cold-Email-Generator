import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from candidate_profile import CANDIDATE_PROFILE


# Load environment variables from .env
load_dotenv()


# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0.3
)


def generate_email(job, portfolio_links):

    prompt = ChatPromptTemplate.from_template(
        """
You are an AI assistant that writes truthful, concise, and professional
job application cold emails.

CANDIDATE PROFILE

Name: {candidate_name}
Education: {education}
Career Level: {level}
Verified Skills: {candidate_skills}
GitHub: {github}


JOB INFORMATION

Role: {role}
Experience Required: {experience}
Required Skills: {job_skills}
Description: {description}


RETRIEVED PORTFOLIO PROJECTS

{portfolio_links}


IMPORTANT RULES:

1. When describing a portfolio project, use ONLY the project's
   project name, techstack, and link exactly as provided.

2. Never expand, interpret, or guess project names or acronyms.

3. Never attribute candidate-profile skills to a specific project
   unless that skill appears in that project's techstack.

4. Job requirements are NOT proof that the candidate has those skills.

5. Never claim professional experience unless explicitly provided
   in the candidate profile.

6. Never claim that a technology was used in a project unless the
   retrieved project information confirms it.

7. Do not invent achievements, internships, metrics, companies,
   certifications, work experience, or years of experience.

8. If a required job skill is not verified in the candidate profile,
   do not claim that the candidate has that skill.

9. Candidate-profile skills may be mentioned as general skills.

10. Do not say a general candidate skill was used in a particular
    project unless that project's techstack explicitly contains it.

11. Include only relevant retrieved portfolio projects.

12. Include the actual GitHub link for each project mentioned.

13. Keep the email concise, professional, and suitable for sending
    directly to a recruiter or hiring team.

14. Do not include an email address or phone number unless it is
    explicitly provided in the candidate profile.

15. If the project is named "CMS", call it only "CMS".
    Never expand CMS into Content Management System.

16. Do not invent what CMS stands for.

17. Return the email as clean plain text.

18. Do NOT use Markdown formatting.

19. Do not use **bold**, # headings, markdown links, or
    [text](URL) formatting.

20. Write the subject on the first line exactly in this style:
    Subject: Application for <Role> - <Candidate Name>

21. Write all GitHub URLs as normal plain-text URLs.

22. End the email with the candidate's name and GitHub profile.

Return ONLY the final email.
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "candidate_name": CANDIDATE_PROFILE["name"],
            "education": CANDIDATE_PROFILE["education"],
            "level": CANDIDATE_PROFILE["level"],
            "candidate_skills": ", ".join(
                CANDIDATE_PROFILE["skills"]
            ),
            "github": CANDIDATE_PROFILE["github"],

            "role": job["role"],
            "experience": job["experience"],
            "job_skills": ", ".join(job["skills"]),
            "description": job["description"],

            "portfolio_links": portfolio_links
        }
    )

    return response.content.strip()