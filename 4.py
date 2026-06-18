import cohere
import gensim.downloader as api

co=cohere.ClientV2("<cohere_api_key>")
model= api.load("glove-wiki-gigaword-50")

prompt = "Describe the future of artificial intelligence in education"

words=[]
for w in prompt.lower().split():
    if w in model:
        words+=[x[0] for x in model.most_similar(w,topn=2)]
    
enriched_prompt=prompt+" "+" ".join(set(words))

original=co.chat(
    model="command-a-03-2025",
    messages=[{"role":"user","content":prompt}]
)

enriched=co.chat(
    model="command-a-03-2025",
    messages=[{"role":"user","content":enriched_prompt}]
)

print("Original Prompt:\n", prompt)
print("\nOriginal Response:\n", original.message.content[0].text)

print("\nEnriched Prompt:\n", enriched_prompt)
print("\nEnriched Response:\n", enriched.message.content[0].text)