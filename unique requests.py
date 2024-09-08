from datasketch import HyperLogLog


n = int(input())
requests = [input().strip() for _ in range(n)]
hll = HyperLogLog(p=14)

for request in requests:
    hll.update(request.encode('utf8'))

estimated_unique_count = hll.count()
print(int(estimated_unique_count))
