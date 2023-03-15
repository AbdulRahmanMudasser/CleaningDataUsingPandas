from matplotlib import pyplot as plt

x = [23, 43, 21, 56, 78, 54, 88, 99, 100, 181, 19, 154, 161, 132, 123, 4, 56, 73, 29, 30, 20, 55, 41]
y = [111, 31, 12, 56, 78, 54, 88, 99, 100, 170, 19, 41, 67, 29, 30, 49, 16, 101, 29, 107, 20, 23, 41]

# plt.hist(x, y)
plt.bar(x, y)

plt.show()

# from nltk.stem import PorterStemmer
#
# poster_stemmer = PorterStemmer()

# from nltk.tokenize import word_tokenize
# from nltk.probability import FreqDist
#
# fDist = FreqDist()
#
# AI = """Natural Language Processing (NLP) is a branch of Data Science which deals with Text data. Apart from
# numerical data, Text data is available to a great extent which is used to analyze and solve business problems. But
# before using the data for analysis or prediction, processing the data is important. What is NLP for text
# classification? Text classification also known as text tagging or text categorization is the process of categorizing
# text into organized groups. By using Natural Language Processing (NLP), text classifiers can automatically analyze
# text and then assign a set of pre-defined tags or categories based on its content."""
#
# AI_tokens = word_tokenize(AI)
#
# for word in AI_tokens:
#     fDist[word.lower()] += 1
#
# print(fDist)

# from nltk.corpus import gutenberg
#
# hamlet = gutenberg.words()
#
# for word in hamlet[0:500]:
#     print(word, sep=' ', end=' ')

# from nltk import word_tokenize, sent_tokenize
#
# message = "I will walk 500 miles and I would walk 500 more, " \
#        "just to be the man who walks a thousand miles to fall down at your door!"
#
# # tokenization
# print(word_tokenize(message))
# print(sent_tokenize(message))

# import pandas as pd

# # reading csv file
# df = pd.read_csv('venv/resource/DataSet.csv')

# # read a specific location
# print(df.iloc[2, 3])

# # read each row
# print(df.iloc[1])
# print(df.iloc[1:4])

# # read each column
# print(df['Calories'])
# print(df['Calories'][0:5])
# print(df[['Calories', 'Duration']])

# # read headers
# print(df.columns)

# # convert data into a correct format
# df['Date'] = pd.to_datetime(df['Date'])
#
# # removing the row with empty/null value
# df.dropna(subset=['Date'], inplace=True)
#
# # replacing wrong value
# df.loc[7, 'Duration'] = 45
#
# print(df.to_string())
