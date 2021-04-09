from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import wget
import os

class Downloader:

    def __init__(self, url_list):
        self._filenames = multithreading(download_txt, url_list)
        self._index = 0

    def __iter__(self):
        return self._filenames

    def __next__(self):
        try:
            item = self._filenames[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return item

    def urllist_generator(self):
        yield from self._filenames

    def avg_vowels(self, filename):
        vowels = "aeiouyæøå"
        with open(filename, 'r') as file:
            words = file.read().replace('\n', '').lower().split('***')[2].split(' ')
            vowel = []
            for word in words:
                vowel.append([1 for char in word if vowels.__contains__(char)])
            idk = [sum(count) for count in vowel if not count == []]
            return sum(idk)/len(idk)

    def hardest_read(self):
        hardness = multiprocess(self.avg_vowels, self._filenames)
        hardness_dict = {hardness[i]: self._filenames[i] for i in range(len(hardness))}

        sorted_dicto = sorted(hardness_dict.items(), key=lambda item: item[1])
        return sorted_dicto[-1]


def download_txt(url):
    filename = os.getcwd() + "/data/" + os.path.basename(url)
    if os.path.exists(filename):
           os.remove(filename)
    return wget.download(url, out='data')

def multithreading(func, args, workers=5):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)

def multiprocess(func, args, workers=multiprocessing.cpu_count()):
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)