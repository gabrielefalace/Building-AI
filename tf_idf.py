text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def compute_term_frequency(doc):
    result = []
    for word in doc:
        matches = list(filter(lambda x: x==word, doc))
        freq = len(matches)/len(doc)
        result.append(freq)
    return result

def compute_document_frequency(word, docs):
    total = 0
    count = 0
    for doc in docs:
        total = total + len(doc)
        count = list(filter(lambda x: x==word, doc))
    return count/total


def main(text):
    # tasks your code should perform:

    docs = [line.lower().split() for line in text.split('\n')]

    unique_words = set()
    for doc in docs:
        for word in doc:
            unique_words.add(word)
    

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    term_frequencies = [[]]*len(docs)
    for i, doc in enumerate(docs):
        term_frequencies[i] = compute_term_frequency(doc)

    print(term_frequencies)

    document_frequencies = []
    for word in unique_words:
        document_frequencies.append(compute_document_frequency(word, docs))


    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.


main(text)

