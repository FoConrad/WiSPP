

class Tokenizer(object):
    pass

def tokenize(read_callable):
    return Tokenizer(read_callable)

def run(file_name: str):
    return tokenize(file_name)

def main():
    print('Running')
