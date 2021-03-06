# -*- coding: utf-8 -*-
"""language translator using googletrans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10VeDm-Vt65qmbhH_NLcLP1kX5HFfGXVE
"""

pip install googletrans==3.1.0a0

from googletrans import Translator

text = '''  Pour souvent, quand sur mon canapé je mens
D'humeur vacante ou songeuse,
Ils clignotent sur cet œil intérieur
Quel est le bonheur de la solitude;
Et puis mon cœur se remplit de plaisir,
Et danse avec les jonquilles. '''

translator = Translator(service_urls=['translate.googleapis.com'])

lang = translator.detect(text)
print(lang)
print(' ')

translated = translator.translate(text, dest = 'en')

print(translated.text)

