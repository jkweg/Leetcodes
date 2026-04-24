class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """

        freq = {'L' : 0 , 'R': 0 , '_': 0}

        for move in moves:
            freq[move] += 1
        
        return abs(freq['L'] - freq['R']) + freq['_']
        
        