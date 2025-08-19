from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

corpus = [
    'I love the book',
    'this book was not so great',
    'the fit was great',
    'i love the shoes'
]

books = 'Books'
clothing = 'Clothing'

categories = [books, books, clothing, clothing]

# vectorizer = CountVectorizer()
vectorizer = CountVectorizer(ngram_range=(1, 2))
# vectorizer = CountVectorizer(ngram_range=(1, 4))

vectors = vectorizer.fit_transform(corpus)  # gives words and vectors

print(vectorizer.get_feature_names_out())
print(vectors.toarray())

clf = SVC(kernel='linear')  # create model
clf.fit(vectors, categories)  # train model

test_corpus = [
    "I love this read",  # book
    "such a nice hat",  # clothing
    "what a great book"  # book
]

test_categories = [books, clothing, books]  # correct answers (y)

# only give vectors, not words, to match the existing list of words
test_x = vectorizer.transform(test_corpus)
print(clf.predict(test_x))  # clothing, clothing, book

# check percentage correct
print(clf.score(test_x, test_categories))
print(f'{clf.score(test_x, test_categories)*100}%')
