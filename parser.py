import csv

import nltk
import os
from nltk import word_tokenize
from collections import defaultdict
from collections import Counter
from nltk.corpus import stopwords
from io import open
import operator


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

class Parser:
    def __init__(self):
        pass

    def clean_files(self, path):
        def filter_s(s):
            return not ("-->" in s or len(s.strip()) == 0)

        documents = ""
        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                if filename.endswith('.vtt'):
                    with open(os.sep.join([dirpath, filename]), "r") as f:
                        print filename
                        try:
                            for i in range(2):
                                next(f)
                            header_lang = next(f)
                            if header_lang.strip() != "Language: en":
                                continue
                            filtered = filter(lambda x: filter_s(x), f)
                            filtered = ' '.join(map(lambda x: x.strip().lower(), filtered))

                            documents += filtered + "\n"
                        except StopIteration:
                            continue
        return documents

    def read_pos_group(self, filename):
        with open(filename, "r", encoding="utf8") as csv_file:
            lines = csv.reader(csv_file, delimiter="\t")
            pos_group = {line[1]: line[0] for line in lines}
        return pos_group

    def run(self, text, filename, filename_sorted_words):
        tokenized_text = word_tokenize(text)
        filtered_words = list(filter(lambda word: word not in stopwords.words('english'), tokenized_text))
        tag = nltk.pos_tag(filtered_words)

        pos_group = self.read_pos_group(filename)
        tag = [(word, pos_group[pos]) for word, pos in tag if pos in pos_group]
        tag_groups = defaultdict(list)
        for word, pos in tag:
            tag_groups[pos].append(word)

        tag_groups_counts = dict(map(lambda (x, y): (x, dict(Counter(y))), tag_groups.iteritems()))
        sorted_tag_groups_counts = dict(map(lambda (x, y):
                                            (x, sorted(y.items(), key=operator.itemgetter(1), reverse=True)),
                                            tag_groups_counts.iteritems()))

        with open(filename_sorted_words, "w") as f:
            for pos, word_count in sorted_tag_groups_counts.iteritems():
                f.write(unicode(pos))
                for word, count in word_count[0:100]:
                    f.write("\t" + '\t'.join([unicode(word), unicode(count)]))
                f.write(unicode("\n"))
        print sorted_tag_groups_counts


if __name__ == '__main__':
    parser = Parser()
    filtered = parser.clean_files("youtube_transcripts")
    # filtered = parser.clean_files("Uploads from Nike")
    parser.run(filtered, "configs/pos/groups.csv", "configs/pos/sorted_words_random_videos.csv")
    # parser.run(filtered, "configs/pos/groups.csv", "configs/pos/sorted_words_ads_videos.csv")
    # parser.read_pos_group("configs/pos/groups.csv")
