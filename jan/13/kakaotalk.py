chat = []
f = open('KakaoTalk_20210112_0314_25_973_group.txt', 'r', encoding='utf-8')
while True:
    tmp = f.readline()
    if tmp == '':
        break
    chat.append(tmp.strip())
f.close()

# 스터디 멤버List
member = ['김태훈', '백승민', '신희승', '이용빈', '이한진', '전가배', '정건',
          '정연재', '정현진', '현승민']
# 멤버별 대화량
conversations_number = {i: 0 for i in member}
# 멤버별 이모티콘 전송량
emoticon_frequency = {i: 0 for i in member}
# 멤버별 사진 전송량
pictures_frequency = {i: 0 for i in member}
# 멤버별 대화 삭제량
delete_frequency = {i: 0 for i in member}
# 날짜별 대화수
date_conversations = {}
# 시간대별 대화수
time_conversations = {i: 0 for i in range(24)}
# 단어 등장수
word_frequency = {}

# --------------------- 위 코드는 만지지 말아주세요. 각 dict와 list가 초기화되어있습니다.

# 아래 print 코드는 chat과 dict에 어떤 데이터가 들어가있는지 확인해보시고
# 지우시면 됩니다.
print(*chat, sep='\n')
print(conversations_number)
print(emoticon_frequency)
print(pictures_frequency)
print(delete_frequency)
print(delete_frequency)
print(date_conversations)
print(time_conversations)
print(word_frequency)
