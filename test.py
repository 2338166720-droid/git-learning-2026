print("Hello Git")
import numpy as np


class MatCalculate:

    # 初始化矩阵
    def __init__(self, matrix_data):

        self.matrix = np.array(matrix_data)
        self.shape = self.matrix.shape
        self.rows = self.shape[0] if len(self.shape) > 0 else 0
        self.cols = self.shape[1] if len(self.shape) > 1 else 0
        self.row_vectors = (
            [self.matrix[i, :] for i in range(self.rows)] if self.rows > 0 else []
        )
        self.col_vectors = (
            [self.matrix[:, i] for i in range(self.cols)] if self.cols > 0 else []
        )

    # 数乘
    def scalar_multiply(self, scalar):

        return scalar * self.matrix

    # 矩阵乘法
    def matrix_multiply(self, other_matrix):

        if isinstance(other_matrix, MatCalculate):
            other = other_matrix.matrix
        else:
            other = np.array(other_matrix)

        # 检查是否可以相乘
        if self.cols != other.shape[0]:
            print(
                f"矩阵无法相乘：第一个矩阵列数({self.cols})与第二个矩阵行数({other.shape[0]})不相等"
            )
            return None

        return np.matmul(self.matrix, other)

    # 基变换
    def basis_transform(self, coordinates, basis_matrix):

        coords = np.array(coordinates)

        if isinstance(basis_matrix, MatCalculate):
            basis = basis_matrix.matrix
        else:
            basis = np.array(basis_matrix)

        try:
            # 求解线性方程组：basis * u = coords
            u = np.linalg.solve(basis, coords)
            return u
        except np.linalg.LinAlgError as e:
            print(f"基变换失败：{e}")
            return None

    # 逆矩阵
    def inverse(self):

        try:
            if self.rows != self.cols:
                print("只有方阵才能求逆")
                return None
            return np.linalg.inv(self.matrix)
        except np.linalg.LinAlgError as e:
            print(f"矩阵不可逆：{e}")
            return None

    # 特征值和特征向量
    def eigenvalues_eigenvectors(self):

        try:
            if self.rows != self.cols:
                print("只有方阵才能求特征值和特征向量")
                return None, None
            # 使用numpy的eig函数替代scipy的eig函数
            eigenvalues, eigenvectors = np.linalg.eig(self.matrix)
            # 将复数结果转换为实数（如果虚部很小）
            if np.allclose(eigenvalues.imag, 0):
                eigenvalues = eigenvalues.real
            if np.allclose(eigenvectors.imag, 0):
                eigenvectors = eigenvectors.real
            return eigenvalues, eigenvectors
        except Exception as e:
            print(f"计算特征值和特征向量失败：{e}")
            return None, None

    # 施密特正交化
    def gram_schmidt_orthogonalization(self):

        if len(self.shape) != 2:
            print("输入矩阵必须是二维的")
            return None

        # 转换为浮点类型矩阵
        A = self.matrix.copy().astype(np.float64)
        num_cols, num_rows = A.shape

        # 初始化正交矩阵Q
        Q = np.zeros_like(A, dtype=np.float64)

        for i in range(num_cols):
            # 取出当前列
            v = A[i, :].copy()

            # 对前面的列进行处理，确保正交
            for j in range(i):
                q = Q[j, :]
                v -= np.dot(v, q) * q

            # 检查向量是否为零向量
            norm = np.linalg.norm(v)
            if norm < 1e-10:
                print(f"第{i+1}列与前面的列线性相关，无法完成正交化")
                return None

            # 归一化
            Q[i, :] = v / norm

        return Q

    # 矩阵求秩
    def rank(self):
        return np.linalg.matrix_rank(self.matrix)

    # 矩阵转置
    def transpose(self):
        return self.matrix.T

    def __str__(self):
        return str(self.matrix)


print("在提交过之后，对本程序进行第二次提交！")
