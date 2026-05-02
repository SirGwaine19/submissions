class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quicksorterhelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quicksorterhelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        pivot = arr[e]
        left = s
        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        arr[left], arr[e] = arr[e], arr[left]
        self.quicksorterhelper(arr, s, left - 1)
        self.quicksorterhelper(arr, left + 1, e)