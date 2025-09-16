# jobs.py
JOBS = [
    {
        "job_id": 1,
        "title": "Video Editor (Premiere Pro) - Entertainment/Lifestyle & Vlogs",
        "description": "Video Editor with Adobe Premiere Pro experience; Splice & Dice, Rough Cut & Sequencing, 2D Animation.",
        "required_skills": ["Adobe Premiere", "Splice & Dice", "Rough Cut", "Sequencing", "2D Animation"],
        "preferred_locations": ["Asia"],  # Asia preferred
        "budget": 2500,
        "rate_type": "monthly",
        "gender_preference": None
    },
    {
        "job_id": 2,
        "title": "Producer/Video Editor (TikTok) - Jenn",
        "description": "Producer/Video Editor — strong TikTok experience, Storyboarding, Sound Designing, Rough Cut & Sequencing, Filming.",
        "required_skills": ["TikTok", "Storyboarding", "Sound Designing", "Rough Cut", "Sequencing", "Filming"],
        "preferred_locations": ["New York", "US"],
        "budget": [100, 150],  # hourly range
        "rate_type": "hourly",
        "gender_preference": "Female"
    },
    {
        "job_id": 3,
        "title": "Chief Operations Officer - Ali Abdaal",
        "description": "COO for productivity/education channel: Strategy, Consulting, Business Operations, high energy and passion for educational content.",
        "required_skills": ["Strategy", "Consulting", "Business Operations", "Operations"],
        "preferred_locations": [],  # open
        "budget": None,
        "rate_type": None,
        "gender_preference": None
    }
]

def get_job_by_id(job_id):
    for j in JOBS:
        if j["job_id"] == job_id:
            return j
    return None

def list_jobs():
    return JOBS
