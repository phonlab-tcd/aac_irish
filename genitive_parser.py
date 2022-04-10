import requests
import re

def apply_changes(text,errors):
    pass

def genitive_parser(text):
    url = f'https://phoneticsrv3.lcs.tcd.ie/gramsrv/api/grammar?text={text}&check=genitive'
    errors = requests.get(url).json()
    return text, errors

def main():
    x,y = genitive_parser("fear an post hata an fear")
    print(x,y)
    x,y = genitive_parser("hata an fear")
    print(x,y)
    x,y = genitive_parser("fear an post")
    print(x,y)

if __name__ == "__main__":
    main()