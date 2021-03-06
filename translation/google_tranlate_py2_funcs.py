"""
Simple funtions to use google tranlate API from a python script

functions included:
translate_source: returns tranlsated text without needing to specify the source language.
get_trans: returns tranlsated text
get_lang: returns language of inputted text
get_possible_langs: returns languages available to translate to and from

"""
import json
import requests

def translate_source(source_text, key=None):
    """
    Inputs:
    source_text - source text as a string 
    key - google api key, needed or function will raise and error

    returns  translated string
    """
    if not key:
        raise Exception( "You dont have a key")
    lang = get_lang_list(source_text, key)
    trans =  get_trans_(source_text, key, lang)
    return trans['data']['translations'][0]['translatedText']

def get_trans_(source_text, key=None , source_lang='',target_lang='en' ):
    """
    Inputs:
    source_text - source text as a string 
    key - google api key, needed or function will raise and error
    target_lang - target language, defaults to 'en' - english
    source_lang - source language, defaults to '' (detect), can also be entered
                  as a string or iterable of strings, size must agree with source_text

    returns dictionary with keys of source_text, values of translated text
    """
    if not key:
        raise Exception( "You dont have a key")
    url_shell = 'https://www.googleapis.com/language/translate/v2?key={0}&source={1}&target={2}&q={3}'
    url = url_shell.format(key, source_lang, target_lang, source_text)
    response = requests.get(url)    
    trans_text = json.loads(response.text)
    for key in trans_text.keys():
        if key == "error":
            raise Exception( "Bad source string.The Json returned from the google  api has 'error' as it's key value")
    return trans_text
    
#this def is not used presently
def get_lang_list(source_text, key=None, print_meta_data=False):
    """
    Inputs:
    source_text - source text as a string
    key - google api key, needed or function will raise and error

    returns list of language identifiers
    """
    #set up url request to google translate api
    if not key:
        raise Exception( "You dont have a key")
    url_shell = 'https://www.googleapis.com/language/translate/v2/detect?key={0}&q={1}'
    url = url_shell.format(key, source_text)
    response = requests.get(url)
    lang_json= json.loads(response.text)
    source_lang = lang_json['data']['detections'][0][0]['language']

#        if print_meta_data:
#            print 'Is detection reliable: {0}'.format(data_dict['data']['detections']['isReliable'])
#            print 'Confidence: {0}'.format(data_dict['data']['detections']['confidence'])
#
    return source_lang

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


