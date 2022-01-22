import requests

def an_gramadoir(text):
    url = 'https://abair.ie/cgi-bin/api-gramadoir-1.0.pl'
    myobj = {'teanga': 'en',"teacs":f"{text}"}
    errors = requests.post(url, data = myobj)
    return errors


def main():
    example = an_gramadoir("Dia Duit.")
    print("\n".join([str(e) for e in example.json()]))

if __name__ == "__main__":
    main()