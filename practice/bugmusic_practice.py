from bs4 import BeautifulSoup
from urllib.request import urlopen                 # import 할때 소문자 = 함수
import urllib.parse

'''
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.    ②순위
"lxml" : 매우 빠르고 유연합니다.                                          ①순위; 제일 빠름
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.                        ②순위
'''


class Bugmusic(object):

    def __init__(self, url):                     # def __init__ : 생성자
        self.url = url                           # .url : 인스턴스 변수    / =url : (local) 변수

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')                   # 메소드    / None: null이랑 같음
        # n_artists = 0
        # n_title = 0
        _ = 0
        artists = soup.find_all(name='p', attrs={'class':'artist'})
        titles = soup.find_all(name='p', attrs={'class':'title'})
        print(f'List size is {len(artists)}')
        for i, j in zip(artists, titles):
            _ += 1
            print(f"Rank {str(_)} Artist: {i.find('a').text}, Title: {j.find('a').text}")


def main():
    # 20210720
    # 16

    '''     Bugmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
                     f'chartdate={input("Input Date")}&charthour={input("Input Hour")}').scrap()   '''

    Bugmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
             f'chartdate={"20210721"}&charthour={"09"}').scrap()


if __name__ == '__main__':
    main()




'''
        for i, j in enumerate(artists):                                 # name='p' : 'p'=태그
            _ += 1
            print(f"Rank {str(_)}Artist: {j.find('a').text}, Title: {titles[i].find('a').text}")
         n_artists += 1
            print(str(n_artists) + " Rank")
            # print(str(n_title)+"Name")
            print("Artist : "+ i.find('a').text+' - '+ls2[n_title].find('a').text)
            n_title += 1
        # print("*"*100)
        ls = soup.find_all(name='p', attrs={'class':'title'})
        print(f'List size is {len(ls)}')
        for i in ls:
            n_title += 1
            print(str(n_title)+"Rank")
            print("Title : "+ i.find('a'.text))
        # print(f'{self.url}')
'''

