from typing import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="050"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc066_a".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  from collections import Counter
  mod=10**9+7
  N=int(input())
  A=list(map(int,input().split()))
  c=Counter(A)
  ans=pow(2,N//2,mod)
  if N%2==0:
    for i in range(N//2):
      if c[2*i+1]!=2: ans=0
  else:
    for i in range(N//2):
      if c[2*i+2]!=2: ans=0
    if c[0]!=1: ans=0
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])