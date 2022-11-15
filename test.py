from heapq import heapify, heappush, heappop
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
from itertools import combinations, product, permutations
from bisect import bisect_left, bisect_right
from functools import lru_cache
from sys import stdin, stdout # for input /output
import copy
import math
import array as arr
from heapq import heappop, heappush
import time
# import sys
# sys.setrecursionlimit(100000)
####################
# stdin = open("testcase.txt")
# def input():
	# 	return stdin.readline().strip()

#####################################################################

class FastIO:

	@classmethod
	def input(cls):
		from sys import stdin
		x = stdin.buffer.readline().decode().strip()
		return x

	@classmethod
	def integer_list(cls):
		return list(map(int, cls.input().split()))

	@classmethod
	def print(cls, s = "", end = "\n"):
		from sys import stdout
		stdout.write(str(s) + end)

	@classmethod
	def flush(cls):
		from sys import stdout
		stdout.flush()


####################################################################

class SegmentTree:
	def __init__(self, data, default=0, func=lambda a, b: a + b):
		"""initialize the segment tree with data"""
		""" initial default value for each node """
		""" func which you want to apply to range """
		self._default = default
		self._func = func
		self._len = len(data)
		self._size = _size = 1 << (self._len - 1).bit_length()
 
		self.data = [default] * (2 * _size)
		self.data[_size:_size + self._len] = data
		for i in reversed(range(_size)):
			self.data[i] = func(self.data[2*i], self.data[2*i + 1])
 
	def __delitem__(self, idx):
		""" delete item set item value to its default """
		self[idx] = self._default
 
	def __getitem__(self, idx):
		""" geting item by inx """
		return self.data[idx + self._size]
 
	def __setitem__(self, idx, value):
		""" changing seting value to given index"""
		""" apply function to range """
		idx += self._size
		self.data[idx] = value
		idx >>= 1
		while idx:
			self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
			idx >>= 1
 
	def __len__(self):
		return self._len
 
	def query(self, start, stop):
		"""func of data[start, stop)"""
		start += self._size
		stop += self._size
 
		res_left = res_right = self._default
		while start < stop:
			if start & 1:
				res_left = self._func(res_left, self.data[start])
				start += 1
			if stop & 1:
				stop -= 1
				res_right = self._func(self.data[stop], res_right)
			start >>= 1
			stop >>= 1
 
		return self._func(res_left, res_right)
 
	def __repr__(self):
		return "SegmentTree({0})".format(self.data)

#####################################################################
class BinaryIndexTree(object):
	""" use one indexing """
	def __init__(self, nums):
		n = len(nums)
		self._len = len(nums)
		self.nums = [0 for _ in range(n+1)]
		self.N = [0 for _ in range(n+1)]
		for i, v in enumerate(nums):
			self.__setitem__(i+1, v)

	def _lowbit(self, a):
		return a & -a

	def  __setitem__(self, i, val):
		diff = val - self.nums[i]
		self.nums[i] = val
		while i < len(self.N):
			self.N[i] += diff
			i += self._lowbit(i)

	def __getitem__(self, i):
		# return sum up 0 to i
		ret = 0
		while i > 0:
			ret += self.N[i]
			i -= self._lowbit(i)

		return ret

######################################################################
class DisJointSetsRank():
    def __init__(self,N):
        # Initially, all elements are single element subsets
        self._parents = [node for node in range(N)]
        self._ranks = [1 for _ in range(N)]
    
    def find(self, u):
        while u != self._parents[u]: 
            # path compression technique
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)
    
    def union(self, u, v):
        # Union by rank optimization
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True
        if self._ranks[root_u] > self._ranks[root_v]:
            self._parents[root_v] = root_u
        elif self._ranks[root_v] > self._ranks[root_u]:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1
        return False


#######################################################################

def integer_list():
	return list(map(int, input().split()))

def pprint(matrix):
	for i in range(len(matrix)):
		print(*matrix[i])


#####################################################
#test case section 
"""
145 --> 11 + 11 + 11 + 111
mod  11*13 + 2



carry = 10*x + req 
x = 1



needed = y

121 --> 

passing carry means --> 10*(x) + carry
"""       


#############################################################
# for manipulating 0 for runing to your local system 1 for online submission


MOD = 10**9+7

ONLINE_JUDGE = 0


def main():
	return
	t = int(input())
	for _ in range(t):
		n = int(input())
		lst = integer_list()

		

		
		



			
			 
			
	


###############################################

if ONLINE_JUDGE:
	input = lambda : stdin.buffer.readline().decode().strip()
else:
	stdin = open("testcase.txt")
	input = lambda : stdin.readline().strip()
	

main()		
	



