import requests
import sys
baseURL ="http://10.13.8.6:2222/.hidden/"

def getList(route):
    req = requests.get(url=route).text
    for line in req.split("\n"):
        if (line.find("<a href=") == 0):
            start = line.find('<a href="') + len('<a href="')
            end = line.find('"', start)
            if start != -1 and end != -1:
                ending = line[start:end]
                if ending == "README":
                    readme = requests.get(url = route + "README")
                    if readme.text.find("flag") != -1:
                        print(readme.text)
            getList(route + ending)

def main():
    getList(baseURL)   

if __name__ == "__main__":
    main()