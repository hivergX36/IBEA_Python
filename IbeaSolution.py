import random 
import math 


class IbeaSolution: 
  def __init__(self, nbVariable,nbconstraint,listConstraint):
        
        self.solution = [0 for i in range(nbVariable)]
        self.SumConstraint = [0 for i in range(nbconstraint)]
        self.Obj1 = 0
        self.Obj2 = 0 
        self.rank = 0 
        valid = True 
        fitnessCalculated = False; 
        self.NbVariable = nbVariable
        self.Nbconstraint = nbconstraint
        self.listConstraint = listConstraint


  def sumconstraint(self, matrix):
       self.SumConstraint = [sum([matrix[ind1][ind2] * self.solution[ind2] for ind2 in range(self.NbVariable)])for ind1 in range(self.Nbconstraint)]
       
  def calculatefitnessvalue(self,Price):
        self.Obj1 = sum([Price[0][i] * self.solution[i] for i in range(self.NbVariable)]) 
        self.Obj2 = sum([Price[1][i] * self.solution[i] for i in range(self.NbVariable)]) 
        
  def CheckIndividual(self):
        check = True
        for k in range(self.Nbconstraint):
              print(self.SumConstraint[k])
              if(self.SumConstraint[k] > self.listConstraint[k] or self.SumConstraint[k] == 0):
                    check = False
                    break
        if check == False:
              print("La solution n'est pas admissible")
              self.admissible = False
        else:
              "La solution est admissible"  
              self.admissible = True


        
  def addmutation(self):
        indlistadd = [i for i in range(self.NbVariable) if self.solution[i] == 0]
        if len(indlistadd) < 1:
              print("Il n'y a rien a muté")
        else:
              indice = random.choice(indlistadd)
              self.solution[indice] = 1
        
  def repaire(self):
        indlistadd = [i for i in range(self.NbVariable) if self.solution[i] == 1]
        indice = random.choice(indlistadd)
        self.solution[indice] = 0
        
  def checkandrepaire(self,compteur):
        check = True
        for k in range(self.Nbconstraint):
              print(self.SumConstraint[k])
              if(self.SumConstraint[k] > self.listConstraint[k] or self.SumConstraint[k] == 0):
                    check = False
                    compteur += 1 
                    if(compteur < 1):
                          self.repaire()
                          self.checkandrepaire(compteur)
                    break
        if check == False:
              print("La solution n'est pas admissible")
              self.admissible = False
        else:
              "La solution est admissible"  
              self.admissible = True
        
        
   
