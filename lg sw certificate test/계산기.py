import sys
import string

nums = string.digits + string.ascii_uppercase

n = int(input())
A = []
for _ in range(n):
	A.append(list(input().split()))

# for _ in range(N):
	
def tenToBnum(B, n):
	Bnum = ''
	if B == 10:
		return n
	neg = False
	if n < 0:
		neg = True
		n *= -1
	while n > 0:
		Bnum += nums[n%B]
		n //= B
	Bnum = list(reversed(list(Bnum)))
	if Bnum[0] == '0':
		Bnum = Bnum[1:]
	if neg:
		return '-' + ''.join(Bnum)
	return ''.join(Bnum)

def BnumToten(B, n):
	res = 0
	if n == 0:
		return 0
	neg = False
	if n[0] == '-':
		neg = True
		n = n[1:]
	n = list(reversed(list(n)))
	for i in range(len(n)):
		if n[i] <= '9':
			res += int(n[i])*(B**i)
		else:
			tmp = ord(n[i]) - ord('A') + 10
			res += tmp*(B**i)
	if neg:
		res = '-' + str(res)
	# print(res)
	return int(res)
	
for a in A:
	B, S, D = a
	mul = BnumToten(int(B), S) *  BnumToten(int(B), D)
	# print(mul)
	print(tenToBnum(int(B), mul))
	
		