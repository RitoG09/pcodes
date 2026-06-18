import gensim.downloader as api

model=api.load("word2vec-google-news-300")

queen_vector=model["king"]-model["man"]+model["woman"]
similar_words=model.similar_by_vector(queen_vector,topn=3)
print("king-man+woman=",similar_words)

actor_vector=model["actor"]-model["man"]+model["woman"]
similar_words=model.similar_by_vector(actor_vector,topn=3)
print("actor-man+woman=",similar_words)