class LoanRegister:
	def __init__(self,branch,manager,currency):
        self._branch=branch
        self.manager=manager
        self.currency=currency
        self.access_level="Local"
        self.__loans={}
	def record_loan(self,loan_id,category,amount,purpose):
        if category not in ["personal","business","student"] :
            raise ValueError("Invalid loan category")
        if purpose.strip()=="":
            raise ValueError("Purpose cannot be empty")
        self.__loans[loan_id]={
            "id":id,
            "category":category,
            "amount":amount,
            "purpose":purpose.strip(),
            "status":"open"
        }
        return True
	def approve_loan(self,loan_id):
        if loan_id not in self.__loans:
            raise KeyError("Loan not found")
        self.__loans[loan_id]["status"]="approved"
        return True
	def get_open_balance(self):
        t=0
        for i in self.__loans.values():
            if i["status"]=="open":
                t=t+i["amount"]
        return t
	def get_loans_sorted(self):
        return sorted(
            self.__loans.values(),
            key=lambda loan : (-loan["amount"],loan["id"])
        )           
class PriorityLoanRegister(LoanRegister):
    def __init__(self,branch,manager,currency,service_rate):
        super().__init__(branch,manager,currency)
        self.__service_rate=service_rate
        self.access_level="Priority"
    def get_service_rate(self):
        return self.__service_rate
    def record_loan(self,loan_id,category,amount,purpose):
        purpose="[PRIORITY] "+ purpose
        if amount >=5000:
            amount+=75
        return super().record_loan(loan_id,category,amount,purpose)
        
        
            
            
            
            
            
        
        
        
        
        
    
                      

    