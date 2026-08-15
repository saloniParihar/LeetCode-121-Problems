class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int1 = int(a,2)
        int2 = int(b,2)
        result = int1+int2
        new_result = bin(result)[2:]
        return new_result
