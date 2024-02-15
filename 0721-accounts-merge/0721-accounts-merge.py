from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visitedAccount = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []
        
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails_accounts_map[email].append(i) 
                # email linked to account
        
        
        def dfs(acct, emails):
            if visitedAccount[acct]:
                return
            
            visitedAccount[acct] = True
            
            for j in range(1, len(accounts[acct])):
                email = accounts[acct][j]
                emails.add(email)
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)
                    
                    
        for i, account in enumerate(accounts):
            if visitedAccount[i]:
                continue
                
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
                    
                
            
            
            
        return [["1"]]
                
        
        