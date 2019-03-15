from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba


def trans_cn(text, stopwords):
    word_lists = jieba.cut(text)
    print(word_lists)
    mytext_list = []
    # 文本清洗
    for word in word_lists:
        if word not in stopwords and word != " " and len(word) != 1:
            mytext_list.append(word.replace(" ", ""))
    result = ",".join(mytext_list)

    # list =[]
    # list.append(word for word in word_lists if word not in stopwords)
    # result = " ".join(list)
    return result


with open("chinese_stopwords.txt", "r", encoding="UTF-8") as f:
    stopwords = f.read().split("\n")
    print(stopwords)

with open("news.txt") as file:
    text = file.read()
    # print(text)
    words = trans_cn(text, stopwords)

    cloud = WordCloud(font_path="C:/Windows/Fonts/simsun.ttc", background_color="white",
                      min_font_size=15, max_font_size=50).generate(words)
    image_produce = cloud.to_image()
    image_produce.show()
