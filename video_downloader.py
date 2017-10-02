import random

from nltk.corpus import words


class VideoDownloader:
    def __init__(self):
        pass

    def generate_query(self):
        list_of_words = words.words()
        samples = random.sample(list_of_words, 500)
        youtube_urls = [''.join(["https://www.youtube.com/results?q=", query, "&sp=EgIYAVAU"]) for query in samples]
        return youtube_urls

    def write_urls_to_file(self, file_name, youtube_urls):
        with open(file_name, "w") as f:
            for url in youtube_urls:
                f.write(url + "\n")


if __name__ == '__main__':
    video_downloader = VideoDownloader()
    youtube_urls = video_downloader.generate_query()
    video_downloader.write_urls_to_file("youtube_transcripts/random_transcripts.txt", youtube_urls)
