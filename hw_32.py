from collections import Counter
import re

def count_words(file_path_text, file_path_stop_words, top_n):
    f = open(file_path_text)
    text = f.read().lower()
    f.close()
    f_1 = open(file_path_stop_words)
    stop_words = f_1.read()
    f_1.close()
    lst = [i for i in re.findall(r'[A-z\']{2,}', text) if i not in stop_words]
    result = {k: lst.count(k) for k in lst}
    most_comm = sorted(result.items(),key=lambda x: x[1],reverse=True)
    print(most_comm[:top_n])




print(count_words('galaxy.txt', 'stop_words.txt', 10))