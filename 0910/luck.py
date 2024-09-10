from param.ipython import message

if __name__ == '__main__':
    arr = [1,2,3]
    message = ','.join(map(str, arr))
    print(message)

    arr2 = ['1','2','3']
    message2 =','.join(arr2)