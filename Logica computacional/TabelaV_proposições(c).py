print(f' P | Q | R | notP | notQ | R V notQ | notP -> RnotQ | P <-> PRQ')
for a in range(0,2,1):
    for b in range(0,2,1):
        for c in range(0,2,1):
           
            #Condição para P
            if a ==0:
                P='V'
                notP='F'
            else:
                P='F'
                notP='V'
           
            #Condição para P
            if b==0:
                Q='V'
                notQ='F'
            else:
                Q='F'
                notQ='V'
          
            # Condição para R
            if c ==0:
                R='V'
            else:
                R='F'
           
            # R V notQ Disjunção
            if R == 'V' or notQ == 'V':
                RnotQ = 'V'
            else:
                RnotQ = 'F'
            
            #notP -> RnotQ cONDICIONAL
            if notP == 'V' and  RnotQ == 'F':
                
               

