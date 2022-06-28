text2 = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

text = '''This little piggy went to market
This little piggy stayed home
This little piggy had roast beef
This little piggy had none
And this little piggy cried wee wee wee all the way home'''

def manhattan_distance(data, i, j):
    row_i = data[i]
    row_j = data[j]
    distance = 0
    for k in range(min(len(row_i), len(row_j))):
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

    docs = [line.lower().split() for line in text.split('\n')]

    unique_words = set()
    for doc in docs:
        for word in doc:
            unique_words.add(word)

    term_frequencies = [[]]*len(docs)
    for i, doc in enumerate(docs):
        term_frequencies[i] = compute_term_frequency(doc)

    document_frequencies = {}
    for word in unique_words:
        f = compute_document_frequency(word, docs)
        document_frequencies[word] = f

    docs_tf_idf = []
    for j, doc in enumerate(docs):
        doc_tf_idf = single_doc_tf_idf(doc, j, term_frequencies, document_frequencies)
        docs_tf_idf.append(doc_tf_idf)

    max_length = 0
    for doc in docs:
        if len(doc) > max_length:
            max_length = len(doc)
    pad_docs = docs_tf_idf # pad_zeroes(docs_tf_idf, max_length)

    min_dist = np.inf
    pair = None
    for i,x in enumerate(pad_docs):
        for j in range(i+1,len(pad_docs)):
            dist = manhattan_distance(pad_docs, i, j)
            #print("Distance between "+str(i)+ " and "+str(j)+ " is: "+str(dist))
            if dist < min_dist:
                min_dist = dist
                pair = (i, j)
    
    print(pair)
    

main(text2)
