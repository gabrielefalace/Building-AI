text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def manhattan_distance(data, i, j):
    row_i = data[i]
    row_j = data[j]
    distance = 0
    print("Data _ (" + str(i) + ") = ", data[i])
    for k in range(len(data[i])):
        distance = distance + abs(row_i[k] - row_j[k])
    return distance

def compute_term_frequency(doc):
    result = []
    for word in doc:
        matches = list(filter(lambda x: x==word, doc))
        freq = len(matches)/len(doc)
        result.append(freq)
    return result


def compute_document_frequency(word, docs):
    count = 0
    for docu in docs:
        if word in docu:
            count = count + 1
    return count/len(docs)


def single_doc_tf_idf(doc, doc_index, term_frequencies, document_frequencies):
    doc_tf_idf = []
    for i, word in enumerate(doc):
        d_freq = document_frequencies[word]
        t_freq = term_frequencies[doc_index][i]
        entry = t_freq * math.log(1/d_freq, 10)
        doc_tf_idf.append(entry)
    return doc_tf_idf


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
    print("\n\n",term_frequencies)

    document_frequencies = {}
    for word in unique_words:
        f = compute_document_frequency(word, docs)
        document_frequencies[word] = f
    print("\n\n", document_frequencies)


    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    # 
    docs_tf_idf = []
    for j, doc in enumerate(docs):
        doc_tf_idf = single_doc_tf_idf(doc, j, term_frequencies, document_frequencies)
        docs_tf_idf.append(doc_tf_idf)

    print("\n\n TF-IDF Reporesentation:\n",docs_tf_idf)

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.

    min_dist = np.inf
    pair = None
    for i,x in enumerate(docs_tf_idf):
        for j,y in enumerate(x):
            dist = manhattan_distance(docs_tf_idf, i, j)
            if dist < min_dist:
                min_dist = dist
                pair = (i, j)
    
    print("\n\nBest Pair:",pair)


main(text)




