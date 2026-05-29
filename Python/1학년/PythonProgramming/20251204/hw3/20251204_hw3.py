# ----------------------------- 설명 ----------------------------- #
# 총기 클래스 gun을 만들고, 더미 클래스 dummy를 만들어서
# gun 클래스의 shoot 메서드를 통해 더미를 맞추는 시뮬레이션 구현.
# gun 클래스는 정확도(ar), 탄약(bullet) 속성을 가지며,
# shoot(times, dname) 메서드를 통해 더미를 맞추는
# 시도를 할 수 있다. times는 시도 횟수, dname은 더미 객체이다.
# shoot 메서드는 정확도에 따라 더미를 맞출 확률을 계산하고,
# 탄약이 남아있는 동안 시도 횟수만큼 더미를 맞추려 시도한다.
# 더미를 맞추면 "더미가 맞았다!"라는 메시지를 출력하고
# 시도를 종료한다. 탄약이 모두 소진되거나 시도 횟수가 끝나면
# "탄약이 모두 소진되었다."라는 메시지를 출력한다.

import random

class dummy:
    def __init__(self):
        self.hp = 1
class gun:
    def __init__(self, ar = 20, bullet = 8): # ar: accuracy rate
        self.ar = ar
        self.bullet = bullet
        self.damage = 1
    def shoot(self, times, dname): # 문제점: 초기 랜덤값에만 의존, times가 높으면 무조건 적중함.
        if self.ar == 0: # 정확도가 0인 케이스
            print(f"Accuracy rate is 0%. cannot hit.")
            return 0
        else:
            # 1부터, 100/self.ar. ex) 20%이면 100/20 = 5. 5번 중 하나 맞음
            rate = random.randint(1, int(100 / self.ar)) 
        for _ in range(times):
            self.bullet -= 1
            if rate >= (100 / self.ar):
                print(f"{type(dname).__name__} got a bullet! good job!")
                break
            else:
                rate += 1 # 안맞으면 확률 증가
            if _ >= times - 1 or self.bullet <= 0:
                print(f"You ran out of ammo(or chance). try again.")
    def reload(self, bullet = 8):
        self.bullet = bullet
    def leftammo(self):
        print(f"{self.bullet} bullet(s) left.")

dummy1 = dummy()
gunman = gun(100, 1)
gunman.leftammo()
gunman.shoot(3, dummy1)
gunman.leftammo()
gunman.reload()
gunman.leftammo()
print(f"--- 2nd gunman ready ---")
gunman2 = gun(0, 12)
gunman2.shoot(3, dummy1)