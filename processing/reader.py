import pandas as pd
from processing import tokenizer

BLOG_CONTENT = '../data/1_BlogContent.txt'


def read_content_chunk(chunksize):
    return pd.read_csv(BLOG_CONTENT, header=0, sep='\001', chunksize=chunksize)

content_chunks = read_content_chunk(100)
for chunk in content_chunks:
    for idx, row in chunk.iterrows():
        print(' '.join(tokenizer.tokenize(row[1])))
