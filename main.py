from agents.fetcher import fetch_jobs
from agents.matcher import rank_jobs
from agents.writer import generate_cover_letter

if __name__ == "__main__":
    jobs = fetch_jobs("sample_data/jobs.json")
    with open("sample_data/resume.txt") as f:
        resume = f.read()

    ranked = rank_jobs(resume, jobs)
    print("Top matches:")
    for job, score in ranked:
        print(f"{job}: {score:.2f}")

    if ranked:
        generate_cover_letter(resume, ranked[0][0])
