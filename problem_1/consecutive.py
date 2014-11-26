class Consecutive(object):

    def find_count(self, word):
        '''
        Find the letter(s) with maximum count.
        The method employed is as follows:
            * Check if the next letter is same as the one being checked.
            * Update the temporary count for the letter.
            * If the temporary count is equal to that of current maximum occuring letter
                - Add the letter to max_letter list
            * If the temporary count is greater than that of current maximum occuring letter
                - Replace the maximum occuring letter with this one
                - Update the reference count with the temporary count, since this is new maximum count
        '''
        max_letter = []
        ref_count = temp_count = 0
        for index, letter in enumerate(word[:-1]):
            if letter == word[index + 1]:
                temp_count += 1
            else:
                temp_count = 0
            if temp_count == ref_count:
                max_letter.append(letter)
            elif temp_count > ref_count:
                max_letter = [letter]
                ref_count = temp_count

        max_letter.sort()

        return max_letter


if __name__ == '__main__':
    word = raw_input('->')
    print Consecutive().max_consecutive_characters(word)
