# 리스트 []

# # 지하철 칸 별로 10명, 20명, 3명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호 씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탔을때
print(subway.append("하하"))
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 삽입
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 4, 3, 2, 1]
num_list.sort()
print(num_list)