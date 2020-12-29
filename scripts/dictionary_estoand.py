#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# vim: ts=4
###
#
# Copyright (c) 2020 Andalugeeks
# Authors : J. Félix Ontañón <felixonta@gmail.com>

import os
import shutil
import io
import glob
import subprocess

# pip install andaluh
from andaluh import epa

SP = 'spain'
AND = 'andalusia'
SP_PACK_DIR = os.path.join('languages',SP,'pack')
AND_PACK_DIR = os.path.join('languages',AND,'pack')
AND_DICT_DIR = os.path.join(AND_PACK_DIR, 'dictionary')
AND_DICT_ADDONS = os.path.join(AND_PACK_DIR, 'dictionary_and')
AND_RAW_DIR = os.path.join(AND_PACK_DIR,'src','main','res','raw')

# Andaluh variants. EPA = all, VAF = standard EPA 'ç' only.
AND_VARS = ['epa', 'vaf', 'zezeo', 'seseo', 'heheo']

def generate_dicts(spain_dict_fp, and_dicts_fp):
    f = io.open(spain_dict_fp, 'r', encoding="utf-8")
    and_dicts_f = [io.open(x, 'w', encoding="utf-8") for x in and_dicts_fp]

    for line in f:
        items = line.split(u',')
        w, word = items[0].split(u'=')
        f1, flags1 = items[1].split(u'=')
        f2, flags2 = items[2].split(u'=')

        # Add abbreviations as-is
        if flags2 == u'abbreviation':
            for file in and_dicts_f:
                file.write(u' word=' + word + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))
        else:
            and_words = [epa(word, vaf=x) for x in [u'ç', u'z', u's', u'h']]

            for i in range(0, len(and_words)):
                and_dicts_f[i+1].write(u' word=' + and_words[i] + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))

            # AND EPA dict includes all variants
            and_dicts_f[0].write(u' word=' + and_words[0] + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))

            if and_words[1] != and_words[0]:
                and_dicts_f[0].write(u' word=' + and_words[1] + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))
            
            if and_words[2] != and_words[0]:
                and_dicts_f[0].write(u' word=' + and_words[2] + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))
            
            if and_words[3] != and_words[0]:
                and_dicts_f[0].write(u' word=' + and_words[3] + u',f=' + flags1 + u',flags=' + flags2 + u',' + u','.join(items[3:]))

def generate_raw_files(and_dicts_fp):
    # Running in reverse, so the last oasp.combined to be copied in pack dictionary is the standard EPA
    for i in reversed(range(0, len(and_dicts_fp))):
        shutil.copy(and_dicts_fp[i], os.path.join(AND_DICT_DIR, 'aosp.combined'))
        if not os.path.exists(AND_RAW_DIR + '_and'):
            os.mkdir(AND_RAW_DIR + '_and')

        # Is subprocess call making the script linux-dependent?
        p = subprocess.call(["./gradlew", ":languages:andalusia:pack:makeDictionary"])
        if int(p)==0:
            for word_file in os.listdir(AND_RAW_DIR):
                number = word_file.split('.')[0].split('_')[-1]
                # Copying generated files on temp 'raw' dir, as each gradlew command removes them
                shutil.copy(os.path.join(AND_RAW_DIR, word_file),
                    os.path.join(AND_RAW_DIR + '_and', AND + '_' + AND_VARS[i] + '_words_' + number + '.dict'), 
                )
        else:
            print("ERROR. ABORTING OPERATION.")
            return

    # Moving the temp files on 'raw' dir
    shutil.rmtree(AND_RAW_DIR)
    shutil.move(AND_RAW_DIR + '_and', AND_RAW_DIR)

    
if __name__ == '__main__':
    os.chdir('..')

    spain_dict_fp = os.path.join(SP_PACK_DIR, 'dictionary','aosp.combined')
    and_dicts_fp = [os.path.join(AND_DICT_ADDONS, x + '.combined') for x in AND_VARS]

    generate_dicts(os.path.join(spain_dict_fp), and_dicts_fp)
    generate_raw_files(and_dicts_fp)