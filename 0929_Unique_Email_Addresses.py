import numpy as np

def numUniqueEmails(emails):
    mails = []
    for e in emails:
        local, domain = e.split("@")
        if "+" in local:
            i = local.index("+")
            local = local[:i]
        local = local.replace(".", "")
        mails.append(local + "@" + domain)
    return len(set(mails))



if __name__ == '__main__':
    s = [[1,0,1],[1,1,0],[1,1,0]]
    result = numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    print(result)


