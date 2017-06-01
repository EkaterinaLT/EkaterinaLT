import json
import re
import codecs
from collections import counter 


def encoding_the_file(new_file, code_type):
	with codecs.open(file, encoding=code_name) as News:
		rss_new = json.load(News)
		return rss_new

def all_words_from_file(rss):
	all_words = []
	words = counter()
	for news in rss_new['rss']['channel']['data']:
		try:
            tags_removed = tags.sub('', news['description']['__cdata'])
        except TypeError:
            tags_removed = tags.sub('', news['description'])
        words = tags_removed.split(' ')
        all_words.extend(words)
        #print(all_words)

    More_than_six_letters = list(filter(lambda x: len(x[0]) > 6, words.most_common()))[:10]
    return More_than_six_letters

def print_words(filename, words):
	for word in words:
		print('{0} - {1}'.format(word[0], word[1]))

files = [
	{'name': 'newsfr.json', 'encoding': 'iso8859_5'},
	{'name': 'newscy.json', 'encoding': 'koi8-r'},
	{'name': 'newsit.json', 'encoding': 'cp1251'},
	{'name': 'newsafr.json', 'encoding': 'utf-8'}
]

for new_file in files:
	print_words(new_file['name'], count_words(read_file(new_file)))
