import matplotlib.pyplot as plt
import numpy as np

# 특정해 (고정점)
particular_solution = np.array([-1, 1, 0])

# 방향벡터 (자유변수 t에 따라 변하는 부분)
direction_vector = np.array([1, -2, 1])

# t 값 설정
t_values = np.linspace(-5, 5, 100)
solutions = np.array([particular_solution + t * direction_vector for t in t_values])

# 3D 그래프
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 해 공간 그리기
ax.plot(solutions[:, 0], solutions[:, 1], solutions[:, 2], label='해 공간 (직선)', linewidth=2)

# 특수해 점 찍기
ax.scatter(*particular_solution, color='red', label='특수해 (-1, 1, 0)', s=50)

# 방향벡터 표시
ax.quiver(*particular_solution, *direction_vector, length=2, normalize=True, color='green', label='방향벡터')

# 라벨 설정
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')
ax.set_title('벡터 형태의 해 공간 (직선)')
ax.legend()

plt.tight_layout()
plt.show()
