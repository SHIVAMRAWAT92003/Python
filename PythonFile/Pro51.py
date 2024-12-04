with open('file5.txt','r') as f:
    
    f.seek(10)
    data=f.read(5)
    print(data)
    
with open('file6.txt','w') as f:
    f.write("Hello bilye kese hai...")
    
    
with open('file7.txt','w') as f:
    f.write("Hello bilye kese hai...")
    f.truncate(8)
    
    
