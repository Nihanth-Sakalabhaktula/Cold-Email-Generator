from job_parser import extract_job_details
from portfolio import Portfolio
from email_generator import generate_email

job_description = """
We are hiring a Python Backend Developer.

The candidate should have 0-2 years of experience.

Required skills include Python, FastAPI, REST APIs,
PostgreSQL, Git and basic knowledge of Docker.

The developer will build backend services, develop APIs,
work with databases and collaborate with engineering teams.
"""

job = extract_job_details(job_description)

portfolio = Portfolio()
portfolio.load_portfolio()

links = portfolio.query_links(job["skills"])

email = generate_email(job, links)

print("\n=== JOB DETAILS ===")
print(job)

print("\n=== RELEVANT PORTFOLIO ===")
print(links)

print("\n=== GENERATED COLD EMAIL ===\n")
print(email)