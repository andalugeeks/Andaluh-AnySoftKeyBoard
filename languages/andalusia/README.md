Teclao Andalûh
==============

A keyboard for mobile and tablet to express yourself in Andalusian. The QÇERTY layout facilitates writing in Andalûh EPA. With its predictive text and auto-correction: you will fly!

https://andaluh.es/es/teclado-andaluz/

Building
--------

The `/scripts/dictionary_estoand.py` script automatically transcribe the spanish anysoftkeyboard dictionary `aosp.combined` file into andalûh. Let this script to generate the dictionaries and avoid the `makeDictionary` gradle step when building the apk.

After generating the dictionaries, the files tree should look like this:

```
Andaluh-AnySoftKeyBoard$ cd languages/andalusia/pack/src/main/res/
Andaluh-AnySoftKeyBoard/languages/andalusia/pack/src/main/res$ tree
.
├── drawable-hdpi
│   └── ic_status_andalusia.png
├── drawable-mdpi
│   └── ic_status_andalusia.png
├── drawable-xhdpi
│   └── ic_status_andalusia.png
├── drawable-xxhdpi
│   └── ic_status_andalusia.png
├── drawable-xxxhdpi
│   └── ic_status_andalusia.png
├── raw
│   ├── andalusia_epa_words_1.dict
│   ├── andalusia_epa_words_2.dict
│   ├── andalusia_epa_words_3.dict
│   ├── andalusia_heheo_words_1.dict
│   ├── andalusia_heheo_words_2.dict
│   ├── andalusia_seseo_words_1.dict
│   ├── andalusia_seseo_words_2.dict
│   ├── andalusia_vaf_words_1.dict
│   ├── andalusia_vaf_words_2.dict
│   ├── andalusia_zezeo_words_1.dict
│   └── andalusia_zezeo_words_2.dict
├── values
│   ├── andalusian_strings.xml
│   └── andalusia_words_dict_array.xml
└── xml
    ├── andalusian_dictionaries.xml
    ├── andalusian_epa_autotext.xml
    ├── andalusian_heheo_autotext.xml
    ├── andalusian_keyboards.xml
    ├── andalusian_seseo_autotext.xml
    ├── andalusian_vaf_autotext.xml
    ├── andalusian_zezeo_autotext.xml
    └── and_qwerty.xml

8 directories, 26 files
```

Testing
-------

A debug apk can be generated and tested on a phone with:

```
./gradlew :languages:andalusia:apk:installDebug -x makeDictionary
```

Generating signed apk
---------------------

ToDo