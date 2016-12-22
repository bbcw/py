#coding:utf-8

# file = open('E://siren/python/test/open.txt','w')
# file.write('Hello,World!')

# file1 = open('E://siren/python/test')
def text_create(name,msg):
    desktop_path = 'E://siren/python/test/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
#text_create('hello','This is test')

def text_filter(word,censored_word='lame',change_word='***'):
    return word.replace(censored_word,change_word)
#print(text_filter('You are lame'))

def censored_text_create(name,msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)
censored_text_create('Try','Python!lame!lame!')