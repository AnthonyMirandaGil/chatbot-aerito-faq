import fasttext
import numpy as np

model = fasttext.load_model('embedings/cc.es.300.bin')
print(model['retirase'])
