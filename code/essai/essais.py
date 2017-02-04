def tokenisation (lien):
    from nltk.corpus import PlaintextCorpusReader
    tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
    from nltk.corpus import BracketParseCorpusReader
    corpus_root = "lien" 
    file_pattern = "discours.txt" 
    ptb = BracketParseCorpusReader(corpus_root, file_pattern)
    ptb.fileids()
    return void
