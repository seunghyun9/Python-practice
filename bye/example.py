import random
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np

class Example:
    def bugs(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml(이름임)
        # print(soup.prettify())
        # print(Quiz20.found(soup, 'artist'))
        # print(''.join(i for i in [i for i in self.found(soup, j)]))
        # a = [i for i in self.found(soup, 'artist')]
        # a = [i for i in self.found
        # (soup, 'title')]
        ls1 = self.found(soup, 'title')
        ls2 = self.found(soup, 'artist')

        a = [i if i == 0 or i == 0 else i for i in range(1)]  # 수열
        b = [i if i == 0 or i == 0 else i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = {i: j for i, j in zip(ls1, ls2)}
        l = [i + j for i, j in zip(ls1, ls2)]
        l2 = list(zip(ls1, ls2))
        d1 = dict(zip(ls1, ls2))
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        print(dict)
        return dict

        '''
        artists = soup.find_all('p', {'class':'artist'})
        artists = [i.get_text() for i in find]
        # print(type(artists))
        print(''.join(i  for i in artists))
        
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))
        '''

        ''' 
         for i in range(3):
            print(artists[i].text.strip())
        '''

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            # print(type(f'타입: {ls1[i]}'))
            dict[ls1[i]] = ls2[i]  # 키값과 벨류값을 출력함 키값:밸류값 << 출력
        print(dict)

    def print_music_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.found(soup, j)):
                print(f'{i}위 :{j}')
            print('*' * 100)

    @staticmethod
    def found(soup, cls_nm) -> []:
        find = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in find]
        # print(type(artists))

    def melon(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        cls_name2 = ['checkEllipsis', 'ellipsis rank01']
        a2 = [i for i in cls_name2]
        '''
        artists = soup.find_all('span', {'class': 'checkEllipsis'})
        titles = soup.find_all('div', {'class':'ellipsis rank01'})
        titles = [i.get_text() for i in titles]
        artists = [i.get_text() for i in artists]
         #print(type(artists))
        print(''.join(i for i in titles))
        print(''.join(i for i in artists))
        '''
        ls3 = self.found2(soup, 'checkEllipsis')
        ls4 = self.found3(soup, 'ellipsis rank01')
        dict2 = {}
        for i, j in zip(ls3, ls4):
            dict2[i] = j
        print(dict2)
        return dict2

    @staticmethod
    def found2(soup, cls_nm) -> []:
        find = soup.find_all('span', {'class': cls_nm})
        return [i.get_text() for i in find]

    @staticmethod
    def found3(soup, cls_nm) -> []:
        find = soup.find_all('div', {'class': cls_nm})
        return [i.get_text() for i in find]

    def dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')  # 내부적으로 엑셀시트형식으로 만듬
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')  # sep = 구분값 , na_rep=비어있으면공백을둬라
        return None

    @staticmethod
    def askicode(start,end):
        columns = [chr(i) for i in range(start, end)]
        return columns

    def practice1(self) -> {}:
            headers = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://maple.gg/guild/luna/%EC%8A%A4%ED%83%A0'
            req = urllib.request.Request(url, headers=headers)
            soup = BeautifulSoup(urlopen(req).read(), 'lxml')
            cls_name1 = ['', '']