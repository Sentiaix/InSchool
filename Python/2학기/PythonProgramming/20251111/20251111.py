lst = [512, 45, 41, 32, 12, 33]
print(lst)

while True:
    s = input('enter index: ')
    try:
        n = int(s)
        temp = lst[n] # indexError 나면 여기서 걸리고 except로 감
        break
    except ValueError:
        print('Please enter valid int')
    except IndexError:
        print(f'index {n} out of range')
    except:
        n = 0

print(f"{lst[n]}*{lst[n]} = {lst[n]*lst[n]}")