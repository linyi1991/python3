def get_file(filename):
    '''從右邊尋找檔案結尾到 '.' '''
    pos = filename.rfind('.')
    '''pos抓到點，往後一位是檔案副檔名到結尾'''
    return filename[pos + 1:] if pos > 0 else print('No search file')

print(get_file(''))