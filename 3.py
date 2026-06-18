import nltk
import string
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec

# Download resources (only first time)
nltk.download('punkt')
nltk.download('stopwords')

# Sample corpus
corpus = [
    "Diabetes is a chronic disease affecting blood sugar",
    "Hypertension can lead to heart disease and stroke",
    "Patient diagnosed with pneumonia and given antibiotics",
    "Insulin therapy used for diabetes patients",
    "Cardiovascular diseases cause many deaths"
]

# Preprocessing
stop = set(stopwords.words("english"))
data = []

for s in corpus:
    words = [
        i for i in word_tokenize(s.lower())
        if i not in stop and i not in string.punctuation
    ]
    data.append(words)

# Train Word2Vec model
model = Word2Vec(data, vector_size=100, window=5, min_count=1, workers=4)

# Vocabulary
print("Vocab:", model.wv.index_to_key)

# Similar words
print("\nSimilar to 'diabetes':")
print(model.wv.most_similar("diabetes"))

# Analogy
print("\nAnalogy: hypertension + heart - stroke")
print(model.wv.most_similar(positive=['hypertension', 'heart'], negative=['stroke']))

# PCA Visualization
words = model.wv.index_to_key

vec = [model.wv[w] for w in words]
pca = PCA(n_components=2)
res = pca.fit_transform(vec)

plt.figure(figsize=(10, 8))
for i, w in enumerate(words):
    x=res[i,0]
    y=res[i,1]
    plt.scatter(x, y)
    plt.text(x + 0.01, y + 0.01, w)

plt.title("Word Embeddings (PCA)")
plt.grid()
plt.show()