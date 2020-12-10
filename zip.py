def sample(n):
    a = []
    for i in range(1,n+1):
        a.append(i)
    return a

def sq_root(arr):
    b = []
    for i in arr:
        b.append(i*i)
    return b

n = 7
s = sample(n)
sr = sq_root(s)

print("sample input : ", s)
print("sample square root : ", sr)

zipped_list = list(zip(s,sr))
print("zipped_list : ", zipped_list)
zipped_set = set(zip(s,sr))
print("zipped_set : ", zipped_set)
zipped_dict = dict(zip(s,sr))
print("zipped_dict : ", zipped_dict)