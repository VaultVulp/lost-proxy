#!/usr/bin/env python3
"""Just a proxy app for lostfilm RSS."""

import os
from time import sleep

import requests

USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
)


def prepare_folders():
    """ Create required folders. """
    os.makedirs('webroot', exist_ok=True)


def get_rss_feed_text():
    """ Load RSS feed and extract the text from it."""
    data = requests.get('http://retre.org/rssdd.xml', headers={'User-Agent': USER_AGENT})
    data.encoding = 'windows-1251'
    return data.text


def modify_links(text: str) -> str:
    """ Return new string with all 'www.lostfilm.tv' replaced with 'old.lostfilm.tv'. """
    return text.replace('www.lostfilm.tv', 'old.lostfilm.tv')


def save_text_to_file(text: str):
    """ Save updated RSS feed to the file. """
    with open('webroot/rssdd.xml', 'w', encoding='utf-8') as file:
        file.writelines(text)


def main():
    """ Main entry point of the app. """
    while (True):
        prepare_folders()
        text = get_rss_feed_text()
        text = modify_links(text)
        save_text_to_file(text)
        sleep(1800)


if __name__ == '__main__':
    main()
