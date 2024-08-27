binary_str=input('你今天被肏了几次:')
print('尊敬的主人，贱奴我今天被肏了'+binary_str+'次。',end='') #binary_str代表二进制，所以只能回答二进制数
binary_num=int(binary_str,2)
print('尊敬的主人，贱奴我今天被肏了',binary_num,'次。',sep='')