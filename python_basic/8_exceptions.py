import traceback

try:
    input = int(input('輸入整數：'))
    print('{0} 為 {1}'.format(input, '奇數' if input % 2 else '偶數'))
except ValueError:
    print('請輸入阿拉伯數字')
except (EOFError, KeyboardInterrupt):
    print('使用者中斷程式')
except:
    print('不明的程式中斷')
    traceback.print_exc()


try:
    f = open('curruptfile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except IOError as e:
    print('First!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')
