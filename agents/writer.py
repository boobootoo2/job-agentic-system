from openai import OpenAI

client = OpenAI()

def generate_cover_letter(resume, job_title):
    prompt = f"Write a personalized cover letter for the role '{job_title}' based on this resume:\n{resume}"
    resp = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}])
    text = resp.choices[0].message.content
    with open(f"drafts/{job_title.replace(' ', '_')}_letter.txt", "w") as f:
        f.write(text)
    print(f"Generated cover letter for {job_title}")
