# 날짜 동적 크롤링

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST. 스트링 정제 작업
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)  #필요없는 특수문자들 제거
    string = re.sub(r"\'s", " \'s", string)                 #
    string = re.sub(r"\'ve", " \'ve", string)               #I've  -> I 've
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()

driver = webdriver.Chrome("./chromedriver_win32/chromedriver")
driver.implicitly_wait(3)

driver.get('https://www.imdb.com/title/tt4154796/reviews?ref_=tt_ql_3')

driver.find_element_by_xpath('//*[@id="load-more-trigger"]').click()
time.sleep(8)
driver.find_element_by_xpath('//*[@id="load-more-trigger"]').click()
time.sleep(7)
driver.find_element_by_xpath('//*[@id="load-more-trigger"]').click()
time.sleep(9)

time.sleep(1)
req = driver.page_source
# #
bs = BeautifulSoup(req, 'lxml')
#
title_list = bs.findAll('a', 'title')
date_list = bs.findAll('span', 'review-date')
score_list = bs.findAll('span', 'rating-other-user-rating')

for title in title_list:
    print(title.getText())

for date in date_list:
    print(date.getText())

for score in score_list:
    print(score.span.getText())

f = open("./data/review+date.txt", "w", encoding='UTF8')
for i in range(len(title_list)):
    f.write('[score: ' + score_list[i].span.getText() + "]" + " [title: " + clean_str(title_list[i].getText()) + "]"
            + ' [date: ' + clean_str(date_list[i].getText()) + "]" + "\n" + ('=' * 100) + "\n")
f.close()

