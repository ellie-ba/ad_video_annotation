import random

from nltk.corpus import words
import numpy as np


class VideoDownloader:
    def __init__(self):
        pass
    def generate_query(self):
        list_of_words = words.words()
        samples = random.sample(list_of_words, 500)
        youtube_urls =[''.join(["https://www.youtube.com/results?q=",query, "&sp=EgIYAVAU"]) for query in samples]
        return youtube_urls


if __name__ == '__main__':
    video_downloader = VideoDownloader()
    video_downloader.generate_query()