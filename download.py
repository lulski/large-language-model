import urllib.request
#https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/refs/heads/main/ch02/01_main-chapter-code/the-verdict.txt


#https://raw.githubusercontent.com/rasbt/LLMs-from-stratch/refs/heads/main/ch02/01_main-chapter-code/the-verdict.txt
url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/refs/heads/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "the-verdict2.txt"
urllib.request.urlretrieve(url,file_path)
