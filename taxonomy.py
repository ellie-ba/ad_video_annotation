import csv
from collections import defaultdict

import operator


class Taxonomy:
    def __init__(self):
        pass

    def read_files(self, filename):
        pos_words = dict()
        words_count = dict()
        with open(filename, "r") as f:
            lines = list(csv.reader(f, delimiter="\t"))
            for line in lines:
                pos = line[0]
                del line[0]
                words = line[::2]
                counts = line[1::2]
                for l in range(len(words)):
                    words_count[words[l]] = counts[l]
                # print len(words)
                pos_words[pos] = set(words)

        return pos_words, words_count

    def complement_(self, pos_words_ads_old, pos_words_rand, words_count):
        pos_words_ads = defaultdict(dict)
        for pos1, words1 in pos_words_ads_old.iteritems():
            words2 = pos_words_rand[pos1]
            pos_words_ads[pos1] = {s: words_count[s] for s in words1 - words2}
        sorted_pow_count = dict(map(lambda (x, y):
                           (x, sorted(y.items(), key=operator.itemgetter(1), reverse=True)),
                           pos_words_ads.iteritems()))
        return sorted_pow_count

if __name__ == '__main__':
    taxonomy = Taxonomy()
    ads_words, words_count = taxonomy.read_files("configs/pos/sorted_words_ads_videos.csv")
    random_video_words, _ = taxonomy.read_files("configs/pos/sorted_words_random_videos.csv")
    key_words = taxonomy.complement_(ads_words, random_video_words, words_count)
    print key_words