n = 100
diff = pow(sum(list(range(1,n+1))),2)  - sum([x * x for x in range(1,n+1)])
print(diff)