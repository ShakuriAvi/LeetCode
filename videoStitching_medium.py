'''

'''

from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        keymap = {}
        for x in clips:
            for i in range(x[0], x[1]):
                if i not in keymap:
                    keymap[i] = x[1]
                else:
                    keymap[i] = max(keymap[i], x[1])

        count = 0
        start = 0
        while start < time:
            if start not in keymap:
                return -1
            start = keymap[start]
            count += 1
        return count









if __name__ == '__main__':
    # print(Solution().videoStitching([[0,2],[4,6],[8,10],[1,5],[1,9],[5,9]], 10))
    # print(Solution().videoStitching([[0,1],[1,2]], 5))
    print(Solution().videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9))
    print(Solution().videoStitching([[0,4],[2,8]], 5))
    print(Solution().videoStitching([[0,5],[1,6],[2,7],[3,8],[4,9],[5,10],[6,11],[7,12],[8,13],[9,14],[10,15],[11,16],[12,17],[13,18],[14,19],[15,20],[16,21],[17,22],[18,23],[19,24],[20,25],[21,26],[22,27],[23,28],[24,29],[25,30],[26,31],[27,32],[28,33],[29,34],[30,35],[31,36],[32,37],[33,38],[34,39],[35,40],[36,41],[37,42],[38,43],[39,44],[40,45],[41,46],[42,47],[43,48],[44,49],[45,50],[46,51],[47,52],[48,53],[49,54]]
                                    , 50))


'''
TO DO 
        queue = []
        res = []
        clips = sorted(clips, key=lambda x: x[0] and x[1])
        for idx, clip in enumerate(clips):
            if clip[0] == 0:
                queue.append(((clip[0], clip[1]), idx))

        while queue:
            curr, idx = queue.pop(0)
            if curr[-1] >= time:
                res.append(curr)
                continue
            for i in range(idx, len(clips)):
                clip = clips[i]
                if curr[-1] >= clip[0] and curr[-1] < clip[1]:
                    queue.append((curr+(clip[0],clip[1]),i))

        return min([int(len(res)/2) for res in res]) if len(res) > 0 else -1
'''