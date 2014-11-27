from itertools import combinations


class NonaryGame(object):
    '''
    Find all valid combinations based on the given criteria
        - length of digits should be between 3-5, both included
        - one of the digits should be 5
        - the digital root of the digits should be 9
    '''
    nums = [1, 2, 3, 4, 5, 6, 7, 8]

    def _find_root(self, number):
        '''
        Calculate digital root of passed number
            * Get individual digits by finding remainder after dividing by 10
            * Add those digits to get a root value
            * If root value is greater than 9, repeat the process using the root value
        '''
        root = 0
        while number > 9:
            root += (number % 10)
            number /= 10
        root += (number % 10)

        if root > 9:
            return self._find_root(root)

        return root

    def _find_root_4m_list(self, number_list):
        '''
        Calculate digital root of the digits in the passed list.
            * Add digits to get root value
            * If root value is greater than 9, use _find_root method to get the digital root
        '''
        root = 0
        for num in number_list:
            root += num
        if root > 9:
            return self._find_root(root)

        return root

    def _validate(self, number_list):
        '''
        Validate the digit list so that it matches the above specified criteria
            * Check if 5 is present in the list
            * Checks if digital root of the list is 9
        '''
        if 5 not in number_list:
            return False

        if self._find_root_4m_list(number_list) != 9:
            return False

        return True

    def valid_groups(self):
        '''
        Generates list of valid digit list which match the above criteria
            * Loop through allowed size of digit list
            * Generate combinations of allowed digits of allowed size
            * Validate that combination satisfies criteria
            * If valid, add the combination to valid list
            * Sort the valid list and return
        '''
        valid_lst = []
        for size in xrange(3, 6):
            for lst in combinations(self.nums, size):
                if self._validate(lst):
                    valid_lst.append(list(lst))

        valid_lst.sort()
        return valid_lst


if __name__ == '__main__':
    print NonaryGame().valid_groups()
