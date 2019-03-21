import json
import unicodedata


class FileUtil:
    @classmethod
    def readCityFile(cls, path):
        with open(path) as f:
            data = json.load(f)
        return data

    @classmethod
    def writeFile(cls, path, content):
        f = open(path, "w+")
        f.write(json.dumps(content))
        f.close()

