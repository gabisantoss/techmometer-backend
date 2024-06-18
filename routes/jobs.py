from fastapi import APIRouter, FastAPI
from jobspy import scrapers, scrape_jobs
from typing import List 
import numpy as np
from models.job import Job

jobs_router = APIRouter(prefix="/jobs")

@jobs_router.get("/")
def get_jobs():
    jobs = scrape_jobs({
    "site_type": ["linkedin"],
    "search_term": "developer",
    "country": ("brazil", "br", "com.br"),
    "results_wanted": 1
    })
    response = []
    print(f"Found {len(jobs)} jobs")
    jobs = jobs.replace({np.nan: None})
    return jobs.to_dict("records")