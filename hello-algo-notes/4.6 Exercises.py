def digits_plus_one(list):
    one = [1]
    for i in range(len(list)-1, -1,-1):
        if list[i] < 9:
            list[i] += 1
            return list
        elif list[i] == 9:
            list[i] = 0
    return one + list


class ListNode:

    def reverse(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre





