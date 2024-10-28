from gensim.models import word2vec
from gensim.models import fasttext
from tqdm import tqdm

# 데이터 불러오기
data = word2vec.LineSentence('naver_movie.nlp')

# Word2Vec 모델 생성
print("Word2Vec 모델 학습 중...")
w_model = word2vec.Word2Vec(data,
                            vector_size=200,
                            window=8,
                            min_count=2,
                            sg=1)
w_model.save('w_embedding.model')
print("Word2Vec 모델 저장 완료: w_embedding.model")

# FastText 모델 생성
print("FastText 모델 학습 중...")
f_model = fasttext.FastText(data,
                            vector_size=200,
                            window=8,
                            min_count=2,
                            sg=1)
f_model.save('f_embedding.model')
print("FastText 모델 저장 완료: f_embedding.model")

# 유사 단어 검색
while True:
    text = input("검색 단어: ")
    if text.lower() == "exit":
        break
    try:
        print('Positive 유사 단어:', f_model.wv.most_similar(positive=[text]))
        print('Negative 유사 단어:', f_model.wv.most_similar(negative=[text]))
    except KeyError:
        print("단어가 모델에 없습니다.")
