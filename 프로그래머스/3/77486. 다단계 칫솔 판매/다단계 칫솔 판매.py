def calculate(parent, child,cost,res):
    while (cost >= 1):
        res[child] += cost - cost//10
        child = parent[child]
        if (child == '-'):
            break
        cost = cost//10

def solution(enroll, referral, seller, amount):
    answer = []

    res = {}
    parent = {}

    # 딕셔너리로 parent {자식:부모}, res 구현 {셀러:수익}
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        res[enroll[i]] = 0

    for i in range(len(seller)):
        calculate(parent,seller[i],amount[i]*100,res)

    answer = [res[name] for name in enroll]

    return answer