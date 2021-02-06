import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud
from PIL import Image
import numpy as np

if __name__ == '__main__':
    #fname = input('Input file name: ', )
    speeches = ['1981-Ronald-Reagan.txt', '1985-Ronald-Reagan.txt', '1989-George-Bush.txt', '1993-William-Clinton.txt', '2001-George-Bush.txt', '2005-George-Bush.txt', '2009-Barack-Obama.txt', '2013-Barack-Obama.txt', '2017-Donald-Trump.txt', '2021-Joe-Baiden.txt']
    masks = ['Reagan.png', 'Reagan.png', 'BushS.png', 'Clinton.png', 'Bush.png', 'Bush.png', 'Obama.png',  'Obama.png', 'Trump.png', 'Biden.png' ]
    i = 0
    for fname in speeches:
        with open(fname, 'r', encoding='utf-8') as f:
            data = f.read()

        stop_list = stopwords.words('english') + ['us', 'america', 'american', 'nation', 'americans', 'country', 'citizen', 'people']
        mask = np.array(Image.open(masks[i]))
        wordcloud = WordCloud(font_path='arial', mask=mask, stopwords=stop_list,
                              width=mask.shape[1], height=mask.shape[0], max_words=200,
                              background_color='black', contour_width=1, contour_color='white').generate(data)
        i += 1

        plt.figure(figsize=(20, 10), facecolor='k')
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig('{}.png'.format(fname[:fname.find('.')]), facecolor='k', bbox_inches='tight')