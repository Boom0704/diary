from gensim.models import Word2Vec, FastText
from gensim.models import KeyedVectors

# 모델 로드
w_model = Word2Vec.load("w_embedding.model")
f_model = FastText.load("f_embedding.model")

# 두 단어 사이의 유사도 계산 함수
def calculate_similarity(model, word1, word2):
    try:
        similarity = model.wv.similarity(word1, word2)
        print(f"유사도({word1}, {word2}): {similarity:.4f}")
    except KeyError as e:
        print(f"단어가 모델에 없습니다: {e}")

# 유사도 계산 예시
while True:
    text = input("유사도 계산할 단어 2개를 입력하세요 (exit 입력 시 종료): ").split()
    if text[0].lower() == "exit":
        break
    if len(text) == 2:
        calculate_similarity(f_model, text[0], text[1])
    else:
        print("두 개의 단어를 입력해주세요.")
