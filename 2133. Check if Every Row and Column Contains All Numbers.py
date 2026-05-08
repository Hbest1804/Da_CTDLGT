class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        target = set(range(1, n + 1))

        for row in matrix:
            if set(row) != target:
                return False

        for col in range(n):
            column = []

            for row in range(n):
                column.append(matrix[row][col])

            if set(column) != target:
                return False

        return True