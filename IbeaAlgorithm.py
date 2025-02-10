class IbeaAlgorithm():
    
  def __init__(self, NbPop,NbInd):
        """Constructeur de notre classe"""
        self.NbInd = NbInd
        self.NbPop = NbPop
        self.NbVariable = 0 
        self.NbObjectives = 2
        self.NbConstraint = 0 
        self.Population = []
        self.Sample = [] 
        self.PriceVariable = []
        self.Constraint = []
        self.MatrixConstraint = []
        self.indicatorMatrix = []
        self.MatrixIndicator = []
        self.List = []
        
        
        
  def checknumber(self,lignes,indice):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(lignes[indice][compteur1] != '\n' and lignes[indice][compteur2] != '\n'):
              while(lignes[indice][compteur2] != " " and lignes[indice][compteur2] != '\n'):
                    compteur2 += 1
              ParsedList.append(int(lignes[indice][compteur1:compteur2]))
              compteur1 = compteur2 + 1
              compteur2 = compteur1

   
              if compteur1 > len(lignes[indice]) - 1:
                    break
        return ParsedList
 
 
  
  def parseKnapsack(self,text):
      fichier = open(text, "r",encoding="utf8")
      lignes = fichier.readlines()
      tab = [self.checknumber(lignes,indice) for indice in range(len(lignes) - 1)]
      self.NbVariable = tab[0][0]
      self.NbObjectives = tab[0][1]
      self.NbConstraint = tab[0][2]
      self.PriceVariable = [[tab[ind2][ind1] for ind1 in range(self.NbVariable)] for ind2 in range(1,self.NbObjectives + 1)]
      self.MatrixConstraint = [[tab[ind][j] for j in range(self.NbVariable)] for ind in range(3,3 + self.NbConstraint )]
      self.constraint = [tab[-1][ind] for ind in range(self.NbConstraint)]
      

        


      
 
    
  def initPopulation(self):
      self.Population = [Solution(self.NbVariable,self.NbConstraint,self.constraint) for i in range(self.NbPop)]
      for i in range(self.NbPop):
            
            self.Population[i].solution = [random.randrange(0,2) for i in range(self.NbVariable)]
            self.Population[i].sumconstraint(self.MatrixConstraint)
            self.Population[i].CheckIndividual()
            while(self.Population[i].admissible == False):
                  self.Population[i].solution = [random.randrange(0,2) for i in range(self.NbVariable)]
                  self.Population[i].sumconstraint(self.MatrixConstraint)
                  self.Population[i].CheckIndividual()
            self.Population[i].calculatefitnessvalue(self.PriceVariable)
            
            

  def displayProblem(self):
        print("The number of variable is: " , self.NbVariable)
        print("The number of constraint is: " , self.NbConstraint)
        print("The number of objectives is: " , self.NbObjectives)
        print("The vector of price is: " , self.PriceVariable)
        print("The cost Matrix is: " , self.MatrixConstraint)
        print("The constraints are: ", self.constraint)

        

                  
                   
  def displayPopulation(self):
        print("The population is: ")
        for i in range(self.NbPop):
              print(self.Population[i].solution, " ", self.Population[i].Obj1, self.Population[i].Obj2)
              
                      
  def displaySample(self):
        print("The sample is: ")
        for i in range(self.NbInd):
              print(self.Sample[i].solution, " ", self.Sample[i].Obj1, self.Sample[i].Obj2, self.Sample[i].rank)
              
              
    
    def calculateIndicatorMatrix(self):
        max = [0,0,0,0]
        number_individuals = len(self.Population)
        self.indicatorMatrix = [[0 for i in range(number_individuals)] for j in range(number_individuals)]
        for j in range(number_individuals):
            for i in range(j,number_individuals):
                for k in range(self.NbObjectives):
              

        
         

        
         
   
                    
    
                    
              


              
              
  def tounament(self):
        compteur = 0
        while(compteur < self.NbInd):
              AddList = []
              for i in range(2):
                    if len(self.front) > 0:
                          indicefront = random.randrange(0,len(self.front))
                    else:
                          indicefront = 0
                    indicesolution = random.randrange(0, len(self.front[indicefront]))
                    randomIndividual = self.front[indicefront][indicesolution]
                    AddList.append(randomIndividual)
                    
             

              AddList.sort(key = lambda x: x.rank) 
              if AddList[0].rank == AddList[1].rank and AddList[1].crowdingdistance > AddList[0].crowdingdistance:
                    self.Sample.append(AddList[0])
              else:
                    self.Sample.append(AddList[0])
              compteur+=1
              
              
  def crossOverMutation(self):
        ind_Parent1 = random.randrange(0,self.NbInd)
        ind_Parent2 = random.randrange(0,self.NbInd)
        ind_crossover = random.randrange(0,self.NbVariable); 
        children1 = Solution(self.NbVariable,self.NbConstraint,self.constraint)
        children2 = Solution(self.NbVariable,self.NbConstraint,self.constraint)
        children1.solution = [0 for i in range(self.NbVariable)]
        children2.solution = [0 for i in range(self.NbVariable)]
        for i in range(ind_crossover):
              children1.solution[i] = self.Sample[ind_Parent1].solution[i]
              children2.solution[i] = self.Sample[ind_Parent2].solution[i]
        for j in range(ind_crossover, self.NbVariable):

              children1.solution[j] = self.Sample[ind_Parent2].solution[j]
              children2.solution[j] = self.Sample[ind_Parent1].solution[j]
              
        Getmuted = random.randrange(3)
        print("choixmutation: ", Getmuted)
        if Getmuted > 0:
              children1.addmutation()
              children2.addmutation()
              children1.sumconstraint(self.MatrixConstraint)
              children2.sumconstraint(self.MatrixConstraint)
              children1.checkandrepaire(0)
              children2.checkandrepaire(0)
              if children1.admissible == True:
                    self.Sample[ind_Parent1] = children1
                    self.Sample[ind_Parent1].calculatefitnessvalue(self.PriceVariable)
              if children2.admissible == True:
                    self.Sample[ind_Parent2] = children2
                    self.Sample[ind_Parent2].calculatefitnessvalue(self.PriceVariable)
              else:
                    self.Sample[ind_Parent2] = self.Sample[ind_Parent2]
                    
  
  
  
  def UpdatePopulation(self):
        compteur = 0 
        arret = False 
        self.List = [self.Population[i] for i in range(self.NbPop)]
        for i in range(self.NbInd):
              self.List.append(self.Sample[i])
        self.rankList()
        self.frontList()
        self.measurecrowdingdistance()
        self.Population = []
        for i in range(len(self.front)):
              if arret == True:
                    break 
              for j in range(len(self.front[i])):
                    self.Population.append(self.front[i][j])
                    compteur =+ 1 
                    if compteur == self.NbPop:
                          arret = True
                          break
                    
              
              
        


  
        
  def resolve(self, Nbgen):
        self.initPopulation()
        self.computeExtremePoint()
        self.displayPopulation()
        for i in range(Nbgen):
              self.displayPopulation()     

              self.rankPopulation()
              self.displayPopulation()     

              self.definePopulationfront()
     
              self.measurecrowdingdistance()
              self.tounament()              
              NbMutation = random.randrange(self.NbInd)
              self.displaySample()
              for j in range(NbMutation):
                    self.crossOverMutation()
              self.UpdatePopulation()
        self.displayPopulation()     



            
              

   




    
      




        


              
              
         
         




        
        
            
      



     

 
    

           
    
    

        
  
        
  
        

      
             
        
             
             
            
             
            



             
            
            

            
             
          
            

        
        
        




     






    
      
        

