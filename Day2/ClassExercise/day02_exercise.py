# An exercise 

# Two classes:
    #Senator.
        #Name.
        #Bills voted on.
        #Type of vote on bill (pass, fail, abstain)
    #Bill.
        #If bill passed/failed (true/false)
        #Which senators votes pass, fail, or abstain.


class Senator():
  def __init__(self, name):
    self.name = name
    self.bills_voted_on = [] ## list of Bill objects

  def __str__(self): # Print method
      return "%s\n%s" %(self.name, self.bills_voted_on)

  def vote(self, bill, choice):
      # Print announcement of vote.
      print(f"{self.name} votes {choice} on the {bill.title} bill.")
      # Add this bill to list of bills that Senator voted for.
      self.bills_voted_on.append(bill)
      # Update bill object with Senator's vote.
      if choice == "yes":
          Bill(
              title = bill,
              votes["yes"].append(self.name)
              )
      if choice == "no":
          Bill(title = bill,
               votes["no"].append(self.name)
               )
      if choice == "abstain":
          Bill(title = bill,
               votes["abstain"].append(self.name)
               )
      
    #update the bill object--add the senator's name to the the list of yes/no/abstain
    #update the senator object--add this bill to the bills this senator has voted on
    #print an informative message announcing the vote 

# For senator, what bills have they voted on and what are their bills names, and did the senator vote yes, no, or abstain.



class Bill():
  def __init__(self, title):
    self.title = title
    self.votes = {"yes" : [], "no" : [], "abstain" : []}
    self.passed = None

  def __str__(self): # Print method
      return "%s\n%s" %(self.title, self.votes, self.passed)

  def result(self):
    ## update and return the "passed" variable to indicate True/False if the bill passed

# wants to know who votes pass, fail, or abstain.


## should be able to do these things
jane = Senator("Jane")
jack = Senator("Jack")
print(jack)
print(jane)
environment = Bill("Environmental Protection")
print(environment)
jane.vote(environment, "yes")
jack.vote(environment, "no")
environment.result()
print(environment.votes)
print(environment.passed)
print(jack.bills_voted_on[0].passed)
