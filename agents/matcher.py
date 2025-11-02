from openai import OpenAI
import faiss, numpy as np

client = OpenAI()

def embed_text(text):
    resp = client.embeddings.create(model="text-embedding-3-large", input=text)
    return np.array(resp.data[0].embedding, dtype="float32")

def rank_jobs(resume, jobs):
    resume_vec = embed_text(resume)
    job_vecs = [embed_text(job["description"]) for job in jobs]
    index = faiss.IndexFlatIP(len(resume_vec))
    index.add(np.vstack(job_vecs))
    scores, idx = index.search(np.array([resume_vec]), len(jobs))
    return [(jobs[i]["title"], float(scores[0][n])) for n, i in enumerate(idx[0])]
