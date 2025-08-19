from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

# LAB 10
""" You are given a small dataset with 10 short movie reviews. Five reviews 
are positive, five reviews are negative. Your task is to build a model that
can determine the sentiment of the reviews. You will be provided with a
ready-made corpus, categories, and test_corpus:
"""

corpus = [
    "the movie was fantastic and i loved every part of it",
    "an absolute masterpiece with brilliant acting",
    "the film was boring and too long",
    "i really enjoyed the story and the visuals",
    "the plot was terrible and the acting was even worse",
    "what a wonderful experience, highly recommend",
    "not worth my time, very disappointing",
    "a truly great film, i will watch it again",
    "the script was weak and the characters were flat",
    "an amazing journey from start to finish",
    "outstanding performances by all the actors",
    "completely awful, walked out halfway through",
    "one of the best movies i have ever seen",
    "terrible dialogue and poor direction",
    "beautifully crafted with incredible cinematography",
    "boring plot that goes nowhere slowly",
    "excellent storytelling and amazing special effects",
    "worst movie of the year, avoid at all costs",
    "compelling characters and emotional depth",
    "overrated and predictable from start to finish",
    "brilliant screenplay with perfect pacing",
    "disappointing sequel that ruins the original",
    "heartwarming story that touched my soul",
    "confusing plot with terrible editing",
    "spectacular visuals and outstanding soundtrack",
    "painfully slow and incredibly dull",
    "masterful direction and phenomenal acting",
    "cheap production with horrible special effects",
    "engaging from beginning to end, highly recommended",
    "completely forgettable and waste of money",
    "great movie, loved it",
    "hated this film",
    "boring and terrible",
    "absolutely fantastic",
    "amazing and wonderful",
    "awful and disappointing",
    "loved every minute",
    "waste of time",
    "brilliant and excellent",
    "bad and dull"
 ]

categories = [
    'Positive',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Negative',
    'Positive',
    'Positive',
    'Negative',
    'Positive',
    'Negative',
    'Positive',
    'Negative'
]

vectorizer = CountVectorizer(ngram_range=(1, 1), stop_words='english')
vectors = vectorizer.fit_transform(corpus)

clf = SVC(kernel='linear')
clf.fit(vectors, categories)

test_corpus = [
    "the movie was great",
    "i hated the film",
    "a boring and bad story",
    "absolutely loved it"
]

test_categories = ['Positive', 'Negative', 'Negative', 'Positive']

test_data_vectorized = vectorizer.transform(test_corpus)

print(clf.predict(test_data_vectorized))
print(
    f'Models correctness: '
    f'{clf.score(test_data_vectorized, test_categories) * 100}%'
)

# How many of the test sentences were classified correctly?
#  - 50%
# What happens if you change ngram_range from (1,1) to (1,2)?
#  - 50%

# What would happen if you had 1000 reviews instead of 10?
#  - The predictions would probably be more accurate

# Bonus 🌟
# Add your own movie reviews to the corpus and see if the model improves.
# - added a lot of reviews and finally got to 100%
# Try removing stopwords (by adding stop_words="english" in CountVectorizer).
# - did not seem to make any difference with this size corpus 
