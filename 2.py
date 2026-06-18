import gensim.downloader as api
import matplotlib.pyplot as plt
from skeleton.decomposition import PCA

model=api.load("word2vec-google-news-300")

words = ["computer","internet","software","hardware","network", 
         "data","server","database","programming","algorithm"] 

vec=[model[w] for w in words]
pca=PCA(n_components=2)
res=pca.fit_tranform(vec)

for i,w in enumerate(words):
    x,y=res[i]
    plt.scatter(x,y)
    plt.text(x,y,w)
    
plt.title("word embeddings (PCA)")
plt.xlabel("PCA component 1")
plt.ylabel("PCA component 2")
plt.grid()
plt.show()

def similar(word):
    try:
        for w,s in model.most_similar(word,topn=3):
            print(w,round(s,4))
    except:
        print("Word not in vocabulary") 
        
similar("internet")