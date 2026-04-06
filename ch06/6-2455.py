out1, in1 =map(int, input().split())
out2, in2=map(int, input().split())
out3, in3=map(int, input().split())
out4, in4 =map(int, input().split())
cur1_5=in1
cur2_5=cur1_5 + in2 -out2
cur3_5=cur2_5 +in3-out3
cur4_5=cur3_5-out4
maxi=max(cur1_5, cur2_5, cur3_5, cur4_5)
print(maxi)
