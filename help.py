import os


fw = open('source_code.txt', 'w')

f1 = os.listdir()
for i in filter(lambda x: x.endswith('.py'), f1):
    fw.write(i)
    fw.write('\n')

    fr = open(f'./{i}')
    fw.write(fr.read())
    fr.close()
    
    fw.write('\n\n\n')

f1 = os.listdir('./pages')
for i in filter(lambda x: x.endswith('.py'), f1):
    fw.write(f'./pages/{i}')
    fw.write('\n')

    fr = open(f'./pages/{i}')
    fw.write(fr.read())
    fr.close()
    
    fw.write('\n\n\n')

fw.close()
