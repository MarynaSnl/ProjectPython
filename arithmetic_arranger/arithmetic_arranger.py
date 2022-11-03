import re
import pandas as pd

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})
        return True
    
    def withdraw(self, amount, description = ""):
        success = self.check_funds(amount)
        if success:
            self.ledger.append({'amount': -amount, 'description': description})
        return success
                               
    def get_balance(self, all_balance = 0):
        ## 0 - all balance
        ## 1 - deposits
        ## 2 - withdrawals
        sum_balans = 0
        for x in self.ledger:
            sum_tmp = x['amount']
            if (all_balance == 0) or (all_balance == 1 and sum_tmp >= 0) or (all_balance == 2 and sum_tmp < 0):
                sum_balans += sum_tmp
        return sum_balans
                               
    def transfer(self, sum_for_transfer, category_for_transfer):
        success = False
        ## a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
        str_category_for_transfer = category_for_transfer.name
        if self.withdraw(sum_for_transfer, "Transfer to "+ str_category_for_transfer):
            ## should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
            category_for_transfer.deposit(sum_for_transfer, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, summ_for_check):
        tmp_balans = self.get_balance(0)
        return tmp_balans >= summ_for_check
    
    def __str__(self):
        len_str_ex = 30
        len_description = 23
        if len(self.name) > len_str_ex:
            str_introduce = self.name[0:len_str_ex]
        else:
            length_st = int((len_str_ex - len(self.name))/2)
            str_introduce = '*'*length_st + self.name + '*'*length_st
            if len(str_introduce) < len_str_ex:
                str_introduce  = str_introduce  + '*'
        str_introduce = str_introduce + '\n'
        sum_total = 0
        for x in self.ledger:
            sum_str = x['amount']
            sum_total += sum_str
            tmp_list = x['description']
            if tmp_list == []:
                description_1 = "" 
            else:
                description_1 = x['description'][0:len_description] 
            if len(description_1) <= len_description:
                description_1 = description_1 + ' '*(len_description - len(description_1))
            str_introduce = str_introduce + description_1 + str("{:>7.2f}".format(sum_str))  + '\n'    
        str_introduce = str_introduce + 'Total:' + str("{:>7.2f}".format(sum_total))
        return str_introduce

def create_spend_chart(categories):
    bar_chart_str = ""
    if categories == []:
        print("Empty")
    else:
        #count_percent = lambda x: int(round((-1)*x.get_balance(2)/x.get_balance(1)*100,0)/10)*10 if x.get_balance(1)!=0 else 0 
        #count_percent = 
        #name_object = lambda x: x.name
        dd = {x.name: (-1)*x.get_balance(2)  for x in categories}
        total = sum(dd.values())
        if total == 0:
            return ""
     
        len_dd = len(dd)
        df = pd.DataFrame(dd, index =['Proc']) 
        df.values[0] = ((df.values[0] /149.94*100)/10).astype(int)*10      
        fin_str = "Percentage spent by category\n";
        for i in range(100, -10, -10):
            filtr = (df.values[0] >= i)
            fin_str = fin_str + str(i).rjust(3, ' ') + "| "
            for j in filtr:
                if j:
                    fin_str = fin_str + "o  "
                else:
                    fin_str = fin_str + "   "    
            fin_str = fin_str + "\n"
        fin_str = fin_str + "    " + "-"* (3*len_dd + 1) + "\n"
        ###  add columns in first line
        df = pd.concat([pd.DataFrame([df.columns.values], columns=df.columns), df], ignore_index=True)
        max_len = 0
        for i in dd.keys():
            if len(i)> max_len:
                max_len = len(i)
        ## names        
        for i in range(0, max_len):
            fin_str = fin_str + " "*5 
            ###  columns
            for k in range(0, df.shape[1]):
                try:
                    if i == 0:
                        fin_str = fin_str + df.values[0][k][i].title()+ ' '*2
                    else:
                        fin_str = fin_str + df.values[0][k][i]+ ' '*2
                except:
                    fin_str = fin_str + ' '*3   
            fin_str = fin_str + "\n"
    ####  - last   "\n"        
    fin_str = fin_str[:len(fin_str)-2 ]+ ' '
    return fin_str