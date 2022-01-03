import win32api as wapi

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    if 'A' in keys:
        return 'A'
    elif 'D' in keys:
        return 'D'
    elif 'H' in keys:
        return 'H'
    else:
        return 'N'
