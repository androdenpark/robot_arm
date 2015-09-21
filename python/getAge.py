import urllib2,json

__ServerURL__ = "http://9.186.57.38:8800/getPredictInfo"

def getAgeFromServer():
    try:
        responseText=urllib2.urlopen(__ServerURL__).read()
        resopnse=json.loads(responseText)
        if resopnse["success"] :
            return resopnse["age"]
        else:
            return None
    except:
        return None,"er"

if __name__ == "__main__":
    print getAgeFromServer()
    
    
