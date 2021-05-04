import re
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

f = open("C:\\Users\hanjo\PycharmProjects\\kakaoTalkChatCloud\\text.txt", 'r', encoding = 'UTF-8')
file = f.read()

# 카카오톡 대화파일에서 시간과 사용자를 제거하고 텍스트만 남깁니다.
lines = file.splitlines()
newText = ''
for l in lines:
    nl = re.sub('.+ : ', '', l)
    newText += nl + ' '

# 형태소 분석
okt = Okt()

mph = []
mph = okt.pos(newText)

# tag 및 예외 설정하여 넣어주기
wordList = []
for word, tag in mph:
    if tag in ['Noun', 'Adjective'] and word not in ['이모티콘', '사진', '동영상', '샵', '검색', '삭제', '메시지', '대상', '검색', '입니다']:
        wordList.append(word)

# 빈도수별로 정렬하여 40개를 저장
counts = Counter(wordList)
frequentWords = counts.most_common(50)

# WordCloud 생성, 폰트를 지정해야함
wc = WordCloud(font_path="C:\\Windows\\Fonts\\NanumSquareL.ttf",background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(frequentWords))

# wordcloud.jpg 생성
cloud.to_file('wordcloud.jpg')

f.close()