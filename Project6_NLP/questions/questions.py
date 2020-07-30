import nltk
import math
import os
import string
import sys

FILE_MATCHES = 1
SENTENCE_MATCHES = 2


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)


    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens


    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files_dict =dict()

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), "r", encoding='utf8') as f:
            files_dict[filename] = f.read()

    return files_dict


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    contents = [
        word.lower() for word in
        nltk.word_tokenize(document)
        if word not in nltk.corpus.stopwords.words("english")
           # Filter out any word that only contains punctuation symbols ('-', '--') but not ('self-driving')
           and not all(char in string.punctuation for char in word)
    ]
    return contents


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """

    idfs = dict()
    words = set()

    #create set of words in each document
    for filename in documents:
        words.update(documents[filename])


    #iterate through words in each document and find idfs
    for word in words:
        #loop for how many docs contain the word
        f = sum(word in documents[filename] for filename in documents)
        idf = math.log(len(documents) / f)
        idfs[word] = idf

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """

    tfidfs = dict()

    for file in files:
        tfidfs[file] = []
        for word in query:
            tf = files[file].count(word)
            tfidfs[file].append((word, tf * idfs[word]))

    rank = sorted(tfidfs.keys(), key=lambda x: tfidfs[x], reverse=True)
    rank = list(rank)

    return rank[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """

    rank = list()

    for sentence in sentences:
        values = [sentence, 0, 0]

        for word in query:
            if word in sentences[sentence]:
                #matvhing word measure (mwm)
                values[1] += idfs[word]
                #query term density
                values[2] += sentences[sentence].count(word)/ len(sentences[sentence])

        rank.append(values)
        rank = sorted(rank, key=lambda item: (item[1], item[2]), reverse=True)

    return (rank[i][0] for i in range(n))


if __name__ == "__main__":
    main()
