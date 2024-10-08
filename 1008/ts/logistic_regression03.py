
text = ["당신에게 특별한 제안이 있습니다",
        "회원님 당첨되셨어요",
        "회의 일정을 확인해 주세요",
        "할인 쿠폰 드립니다",
        "닉 어제 먹은 점심 메뉴 말고 다른거...",
        "당신의 계좌로 입금 하였습니다.",
        "오빠, 오늘 저녁에 시간 있어요? 같이 나가자. 내 새 아이디 라인(LINE) : xyu0000"]

# 0 : 정상  / 1 : 스팸

labels = [1, 1, 0, 1, 0, 0, 1]


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
vec = TfidfVectorizer()

x = vec.fit_transform(text).toarray()
y = labels
model = LogisticRegression()
model.fit(x, y)

mail = ["요즘 잘 지내세요? 내가 10일에 한국에 너를 찾으러 올게, 너 시간 괜찮아?"]
mail_vec = vec.transform(mail)
pred = model.predict(mail_vec)
print(pred)

if pred == 0:
    print("정상")
else:
    print("스팸")

