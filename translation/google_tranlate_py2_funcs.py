"""
Simple funtions to use google tranlate API from a python script

functions included:
get_trans: returns tranlsated text
get_lang: returns language of inputted text
get_possible_langs: returns languages available to translate to and from

"""
import json
import requests

def get_trans(source_text, key = '', target_lang = 'en', source_lang = ''):
    """
    Inputs:
    source_text - source text as a string or iterable of strings
    key - google api key, needed or function will raise and error
    target_lang - target language, defaults to 'en' - english
    source_lang - source language, defaults to '' (detect), can also be entered
                  as a string or iterable of strings, size must agree with source_text

    returns dictionary with keys of source_text, values of translated text
    """
    #CODE!!

def get_lang(source_text, key = ''):
    """
    Inputs:
    source_text - source text as a string or iterable of strings
    key - google api key, needed or function will raise and error

    returns list of language identifiers
    """
    #CODE!!! 

def get_possible_langs(key = '', target_lang = 'en'):
    """
    Inputs:
    key - google api key, needed to connect to google translate

    returns dictionary of keys as language code in english, values of language name
    """
    #set up url request to google api
    url_shell = 'https://www.googleapis.com/language/translate/v2/languages?key={0}&target={1}'
    url = url_shell.format(key,target_lang)
    response = requests.get(url)

    #parse response
    data_dict = json.loads(response.text)
    lang_list = data_dict['data']['languages']

    data_dict_out = {}
    for lang_dict in lang_list:
        data_dict_out[lang_dict['language']] = lang_dict['name']

    return data_dict_out

