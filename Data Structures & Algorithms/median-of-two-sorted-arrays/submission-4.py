class Solution:
    def get_kth(self, a: List[int], m: int, b: List[int], n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
        # A needs to be smaller than B
        if m > n:
            return self.get_kth(b, n, a, m, k, b_start, a_start)

        # A is empty, get Kth of B
        if m == 0:
            return b[b_start + k - 1]
        # K is 1, A is minimum of both starts
        if k == 1:
            return min(a[a_start], b[b_start])

        # try to get k / 2 th element, bounded by size of array
        i = min(m, k // 2)
        j = min(n, k // 2)

        # A > B, reduce search size of B to look at larger numbers (first i elements invalid)
        if a[a_start + i - 1] > b[b_start + j - 1]:
            return self.get_kth(a, m, b, n - j, k - j, a_start, b_start + j)
        # B >= A, reduce search size of A to look at larger numbers (first j elements invalid)
        else:
            return self.get_kth(a, m - i, b, n, k - i, a_start + i, b_start)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (self.get_kth(nums1, len(nums1), nums2, len(nums2), left) +
                self.get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0