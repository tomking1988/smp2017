import jieba
import zhon.hanzi
import string


def tokenize(text):
    filter_list = zhon.hanzi.punctuation + string.punctuation + ' '
    return filter(lambda word: word not in filter_list, jieba.cut(text))

