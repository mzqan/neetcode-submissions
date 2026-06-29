class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tracking = []
        for i in range (len(position)):
            tracking.append([position[i], speed[i]])
        tracking.sort(reverse=True)

        st = []
        for i in range (len(tracking)):
            time = (target - tracking[i][0]) / tracking[i][1]
            if (i == 0) or (time > st[-1]):
                st.append(time)

        return len(st)



        # 4 > 6 > 8 > 10
        # 1 > 4 > 7 > 10

        # 7 > 8 > 9 > 10
        # 4 > 6 > 8 > 10
        # 1 > 3 > 5 > 7 > 9 > 10
        # 1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 > 9