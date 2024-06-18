from fastapi import FastAPI
from jobspy import scrape_jobs
from routes.jobs import jobs_router
import json
import pandas as pd

app = FastAPI()
app.include_router(jobs_router)

@app.get("/")
async def root():
    jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
    search_term="software engineer",
    location="Dallas, TX",
    results_wanted=20,
    hours_old=72, # (only Linkedin/Indeed is hour specific, others round up to days old)
    country_indeed='USA',  # only needed for indeed / glassdoor
    # linkedin_fetch_description=True # get full description and direct job url for linkedin (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
)
    return jobs.to_json(orient='records', lines=True)