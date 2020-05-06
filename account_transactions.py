# -*- coding: utf-8 -*-
"""Account Transactions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mxar3GYXscbd5VebPiNrQwXg9jLc-Hgr
"""

import datetime
import pytz
class Account:

  @staticmethod

  def _current_time():
    utc_time = datetime.datetime.utcnow()
    return pytz.utc.localize(utc_time)

  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    self.transaction_list = []
    print("Account created for " + self.name)

  def deposit(self,amount):
    if amount >0 :
      self.balance += amount
      self.show_balance()
      self.transaction_list.append((Account._current_time(),amount))

  def withdraw(self,amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      self.transaction_list.append((Account._current_time(),-amount))
    else:
      print("Balance is low")
    self.show_balance()
    
  def show_balance(self):
    print("Balance is {} ".format(self.balance))

  def show_transaction(self):
    for date, amount in self.transaction_list:
      if amount > 0:
        tran_type = "deposited"
      else:
        tran_type = "withdraw"
        amount *= -1
      print("{:5} {} on {} (local time was {})".format(amount, tran_type , date, date.astimezone()))

if __name__ == '__main__':
  Parth = Account("Parth",0)  
  Parth.deposit(1500)
  Parth.withdraw(600)
  Parth.show_transaction()





















