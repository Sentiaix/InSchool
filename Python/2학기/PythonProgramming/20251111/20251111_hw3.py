'''문제 3.
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
int 2개을 입력 받아서 lst[i]*lst[j] 출력. 입력 받은 값이 int이고 인덱스 범위 안에 있을 때까지 입력 요구하는 코드를 except를 사용해서 작성.
Error가 나오면 ValueError인지 IndexError인지 출력.'''

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]

while True:
    s = input("Enter two integers: ")
    try:
        i = 0 # 사실 이 두개 없어도 문제는 없음
        j = 0 
        i, j = map(int, s.split())
        temp1 = lst[i]  # indexError 나면 여기서 걸리고 except로 감
        temp2 = lst[j]
        break
    except ValueError:
        print('Please enter valid int')
    except IndexError:
        print(f'index {i} or {j} out of range')
    except:
        n = 0

print(f"lst[i] * lst[j] = {lst[i]*lst[j]}")