from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Job(BaseModel):
    id: str
    site: str
    job_url: str | None
    job_url_direct: str | None
    title: str | None
    company: str | None
    location: str | None
    job_type: str | None
    date_posted: datetime | None
    interval: str | None
    min_amount: float | None
    max_amount: float | None
    currency: str | None
    is_remote: bool | None
    job_function: str | None
    emails: str | None
    description: str | None
    company_url: str  | None
    company_url_direct: str | None
    company_addresses: str | None
    company_industry: str | None
    company_num_employees: str | None
    company_revenue: str | None
    company_description: str | None
    logo_photo_url: str | None
    banner_photo_url: str | None
    ceo_name: str | None
    ceo_photo_url: Optional[str | None]