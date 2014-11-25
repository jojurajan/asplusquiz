from itertools import combinations


class DigitalRoot(object):
    nums = [1, 2, 3, 4, 5, 6, 7, 8]

    def _find_root(self, number):
        root = 0
        while number > 9:
            root += (number % 10)
            number /= 10
        root += (number % 10)

        if root > 9:
            return self._find_root(root)

        return root

    def _find_root_4m_list(self, number_list):
        root = 0
        for num in number_list:
            root += num
        if root > 9:
            return self._find_root(root)

        return root

    def _validate(self, number_list):
        if 5 not in number_list:
            return False

        if self._find_root_4m_list(number_list) != 9:
            return False

        return True

    def valid_groups(self):
        valid_lst = []
        for size in xrange(3, 6):
            for lst in combinations(self.nums, size):
                if self._validate(lst):
                    valid_lst.append(lst)

        valid_lst.sort()
        return valid_lst


if __name__ == '__main__':
    print DigitalRoot().valid_groups()
