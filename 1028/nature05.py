from gensim.models import FastText, Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 기존에 학습된 FastText 모델 로드
fast_model = FastText.load("f_embedding.model")
# 기존에 학습된 Word2Vec 모델 로드
w_model = Word2Vec.load("w_embedding.model")

# 문장 벡터 계산 함수
def sentence_vector(sentence, model):
    words = sentence.split()
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    return np.mean(word_vectors, axis=0) if word_vectors else np.zeros(model.vector_size)

# 문장 유사도 계산 함수
def calculate_similarity(sentence1, sentence2, model):
    vec1 = sentence_vector(sentence1, model)
    vec2 = sentence_vector(sentence2, model)
    similarity = cosine_similarity([vec1], [vec2])[0][0]
    return similarity

# 사용자로부터 문장 입력받기
sentence1 = input("첫 번째 문장을 입력하세요: ")
sentence2 = input("두 번째 문장을 입력하세요: ")

# 유사도 계산 및 출력
similarity_score = calculate_similarity(sentence1, sentence2, fast_model)
print(f"문장 유사도: {similarity_score:.4f}")
