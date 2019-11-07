import re

with open('regex_sum_180748.txt') as f:
	s = f.read()
	nums = re.findall('[0-9]+', s)

ans = 0
for num in nums:
	ans += int(num)

print(ans) 
