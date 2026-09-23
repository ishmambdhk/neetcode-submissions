class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for n in num_set:
            # Only start counting if 'n' is the beginning of a sequence
            if (n - 1) not in num_set:
                cur_num = n
                cur_len = 1

                # Count forward along the consecutive sequence
                while (cur_num + 1) in num_set:
                    cur_num += 1
                    cur_len += 1

                max_len = max(max_len, cur_len)

        return max_len