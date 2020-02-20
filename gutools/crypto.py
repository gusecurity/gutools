import base64
import hashlib

def compare(data,key=None,checks=None):
    '''
    Checks a dictionary to see if any data is a hashed or encoded
    version of another value in the dictionary.
    '''
    comparisons=[]
    checks=checks or [to_base64,from_base64,md5,sha1,sha512]
    for k,v in data.items():
        if key:
            if key != k:
                for check in checks:
                    if check(v) == data[key]:
                        comparisons.append({
                            'type':check.__name__,
                            'source':key,
                            'similar':k
                        })
        else:
            for ck, cv in data.items():
                for check in checks:
                    if check(cv) == v:
                        comparisons.append({
                            'type':check.__name__,
                            'source':k,
                            'similar':ck
                        })
    return comparisons

def to_base64(string):
    return base64.b64encode(string.encode()).decode()

def from_base64(string):
    try:
        return base64.b64decode(string.encode()).decode()
    except UnicodeDecodeError as e:
        return

def md5(string):
    return hashlib.md5(string.encode()).hexdigest()

def sha1(string):
    return hashlib.sha1(string.encode()).hexdigest()

def sha512(string):
    return hashlib.sha512(string.encode()).hexdigest()