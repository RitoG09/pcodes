import gensim.downloader as api
import cohere

co=cohere.Client("<cohere_api_key>")

model=api.load("word2vec-google-news-300")

def similar_words(word, n=5):
    try:
        return [w for w,_ in model.most_similar(word,topn=5)]
    except:
        return []
    
def generate(seed,words):
    prompt=f"Write a short creative paragraph using '{seed}' and these related words: {', '.join(words)}."
    r = co.chat(model="command-a-03-2025", message=prompt, temperature=0.7, max_tokens=200)
    return r.text.strip()

seed=input("Enter a seed word: ").lower() 
words=similar_words(seed)

if words:
    print("Similar words:", ", ".join(words))
    print("\nGenerated paragraph:\n")
    print(generate(seed,words))
else:
    print("word not found in vocabulary.")