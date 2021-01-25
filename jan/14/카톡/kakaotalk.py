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

for line in chat:  # 한줄씩

    # 파일 맨 앞에 '▶겨울방학 Python 스터디◀ 님과 카카오톡 대화' 이런 부분 건너뛰기.
    if line[0] != '[' and line[0] != '-':
        continue

    # 날짜 받기
    if line[0] == '-':
        g1, *date_info, g2 = line.split()
        date_conversations['-'.join(date_info)] = 0
        continue

    # 나머지는 일반 대화
    line_split = line.split()       # 공백 기준으로 대화분리
    person = line_split[0][1:-1]    # 대화하는 사람

    time = line_split[1:3]          # 아래 코드는 ['오후', [23, 33]]과 같이 대화 시간 나눔
    time[0] = time[0][1:]           # time = ['오전', '11:33]']
    time[1] = list(map(int, time[1][:-1].split(':')))   # time = ['오전', [11, 33]]
    if time[0] == '오후':
        time[1][0] += 12
        if time[1][0] == 24:
            time[1][0] = 0

    talk = line_split[3:]           # 그 뒤 대화

    # 이부분부턴 dict에 추가
    conversations_number[person] += 1               # 한 사람이 대화한 수 +1

    date_conversations['-'.join(date_info)] += 1    # 날짜 대화 +1

    time_conversations[time[1][0]] += 1             # 시간대 대화 +1

    if len(talk) == 1 and talk[0] == '이모티콘':       # 대화가 이모티콘이면 +1
        emoticon_frequency[person] += 1
        continue

    elif len(talk) == 1 and talk[0] == '사진':           # 대화가 사진이면 +1
        pictures_frequency[person] += 1
        continue

    elif ' '.join(talk) == '삭제된 메시지입니다.':   # 대화가 삭제되면 +1
        delete_frequency[person] += 1
        continue

    # 이모티콘, 사진, 삭제에서 continue하는 이유는 해당 단어는 단어 집계에서 제외되어야 하기 때문.

    for i in talk:                                  # 단어별 빈도수 +1
        if i in word_frequency:
            word_frequency[i] += 1
        else:
            word_frequency[i] = 1

# 연산 후 날짜와 시간대 빼고 dict 정렬
conversations_number = dict(sorted(conversations_number.items(),
                                   key=(lambda x: x[1]), reverse=True))
emoticon_frequency = dict(sorted(emoticon_frequency.items(),
                                 key=(lambda x: x[1]), reverse=True))
pictures_frequency = dict(sorted(pictures_frequency.items(),
                                 key=(lambda x: x[1]), reverse=True))
delete_frequency = dict(sorted(delete_frequency.items(),
                               key=(lambda x: x[1]), reverse=True))
word_frequency = dict(sorted(word_frequency.items(),
                             key=(lambda x: x[1]), reverse=True))

print('========== 대화 수 ==========')
f = open('conversations_number.txt', 'w')
for n in conversations_number:
    t = n+'\t'+str(conversations_number[n])
    print(t)
    f.write(t+'\n')
f.close()
print()

print('========== 이모티콘 수 ==========')
f = open('emoticon_frequency.txt', 'w')
for n in emoticon_frequency:
    t = n+'\t'+str(emoticon_frequency[n])
    print(t)
    f.write(t+'\n')
f.close()
print()

print('========== 사진 수 ==========')
f = open('pictures_frequency.txt', 'w')
for n in pictures_frequency:
    t = n+'\t'+str(pictures_frequency[n])
    print(t)
    f.write(t+'\n')
f.close()
print()

print('========== 삭제 수 ==========')
f = open('delete_frequency.txt', 'w')
for n in delete_frequency:
    t = n+'\t'+str(delete_frequency[n])
    print(t)
    f.write(t+'\n')
f.close()
print()

print('========== 날짜별 ==========')
f = open('date_conversations.txt', 'w')
for n in date_conversations:
    t = n+'\t'+str(date_conversations[n])
    print(t)
    f.write(t+'\n')
f.close()
print()

print('========== 시간별 ==========')
f = open('time_conversations.txt', 'w')
for n in time_conversations:
    t = str(n)+'\t'+str(time_conversations[n])
    print(t)
    f.write(t+'\n')
f.close()
print()

# 단어별
f = open('word_frequency.txt', 'w', encoding='utf-8')
for n in word_frequency:
    t = n+'\n'+str(word_frequency[n])
    f.write(t+'\n\n')
f.close()
