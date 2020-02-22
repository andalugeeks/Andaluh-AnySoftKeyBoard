#!/usr/bin/python

import io
from andaluh import epa

spain_dict = '../languages/spain/pack/dictionary/aosp.combined'
andalusia_dict = '../languages/andalusia/pack/dictionary/aosp.combined'

f = io.open(spain_dict, 'r', encoding="utf-8")

with io.open(andalusia_dict, 'w', encoding="utf-8") as file:
    for line in f:
        items = line.split(u',')
        w, word = items[0].split(u'=')
        f1, flags1 = items[1].split(u'=')
        f2, flags2 = items[2].split(u'=')

        epa_word = epa(word)
        zezeo_word = epa(word, vaf='z')
        seseo_word = epa(word, vaf='s')
        heheo_word = epa(word, vaf='h')

        if flags2 == u'abbreviation': 
            file.write(u' word=' + word + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))
        else:
            file.write(u' word=' + epa_word + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))

            if zezeo_word != epa_word:
                file.write(u' word=' + zezeo_word + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))
            
            if seseo_word != epa_word:
                file.write(u' word=' + seseo_word + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))
            
            if heheo_word != epa_word:
                file.write(u' word=' + heheo_word + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))
