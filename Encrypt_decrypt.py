try:
    path = input(r'Enter path of Object: ')
    key = int(input('Enter key for encryption/decryption of object: '))
    print('The path of file : ',path)
    print('Key for encryption / decryption : ',key)
    fin = open(path,'rb')
    ob= fin.read()
    fin.close()
    ob= bytearray(ob)
    for index, values in enumerate(ob):
        ob[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(ob)
    fin.close()
    print('done')
except Exception:
    print('Error caught', Exception.__name__)
