from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited_account = [False]* len(accounts)
        emails_acct_map = defaultdict(list)
        res = []
        
        for i, acct in enumerate(accounts):
            for j in range(1, len(acct)):
                email = acct[j]
                emails_acct_map[email].append(i)
                
        def dfs(acctNum, emails):
            if visited_account[acctNum]:
                return
            visited_account[acctNum] = True
            
            for j in range(1,len(accounts[acctNum])):
                email = accounts[acctNum][j]
                emails.add(email)
                
                for neighbor in emails_acct_map[email]:
                    dfs(neighbor, emails)
        
        for i, acct in enumerate(accounts):
            if visited_account[i]:
                continue
            name, emails = acct[0], set()
            dfs(i, emails)
            res.append([name]+sorted(emails))
        return res