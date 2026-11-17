class LedgerAccount :
    def __init__(self,account_id,owner,opening_balance,reserve_limit=None) :
        self._balance=opening_balance
        self._transactions={"credit":[],"debit":[]}
        self._account_id=account_id
        self.owner=owner
        if reserve_limit==None :
            self.account_type="Basic"
        else :
            self.account_type="Priority"
        	self._reserve_limit=reserve_limit
    def _check_amount(self,amoun=t):
        if amount<0:
            raise ValueError("Amount cannot be negative")
        return True
    def credit(self,amount):
        if amount<0 :
            raise ValueError("Amount cannot be negative")
        self._balance=self._balance+amount
        self._transactions["credit"].append({"amount" : amount})
        return self._balance
    def debit(self,amount):
        fee=0
        if amount<0:
            raise ValueError("Amount cannot be negative")
        if self.account_type=="Priority" and  amount > _reserve_limit :
            raise ValueError("Priority withdrawal exceeds reserve")
        if amount > = 50 :
            fee = 3
        if self._balance < amount + fee :
            raise ValueError("Insufficient funds")
        self._transactions["debit"].append({"amount":amount})
        return self._balance
    def balance(self):
        return self._balance
    def transactions(self,kind=None):
        rs=[]
        if kind==None :
            for k,v in self._transactions.items():
                for rec in v :
                    rs.append(rec)
            rs.sort(key=lambda x : x["amount"],reverse=True)
            return rs
        for k,v in self._transactions.items():
            if k==kind:
                for k,v in self._transactions.items():
                    for rec in v :
                        rs.append(rec)
                rs.sort(key=lambda x : x["amount"],reverse=True)
                return rs
    def largest_transaction(self,kind):
        rs=[]
        for k,v in self._transactions.items():
            if k== kind :
                for rec in v :
                    rs.append(rec)
                return max(rs,key=lambda x : x["amount"])["amount"]
    def reserve_limit(self):
        return self._reserve_limit
        
    
            
        
    
            
                    
                
                
        