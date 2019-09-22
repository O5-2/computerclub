# Leetcode problem: Keys and Rooms (841)

from typing import List

class Solution:
    global keys
    keys = [0]

    def helper(self, rooms: List[List[int]], index: int) -> None:
        global keys
        s = Solution()
        for i in rooms[index]:
            if i not in keys:
                keys.append(i)
                a = s.helper(rooms, i)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        global keys
        keys = [0]
        s = Solution()
        a = s.helper(rooms, 0)
        return (len(keys) == len(rooms))

s = Solution()
print(s.canVisitAllRooms([[1],[2],[3],[]]))
print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
