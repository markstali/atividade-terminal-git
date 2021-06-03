'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
print('Programa para calculo populacional simples.')
while True:
    pop_A = int(input("PopA: "))
    pop_B= int(input("PopB: "))
    cres1 = float(input("Taxa de Crescinento PopA: "))
    cres2 = float(input("Taxa de Crescimento PopB: "))
    if cres2 >= cres1:
            print(f"A taxa de crescimento da 'PopB'não pode ser maior que a taxa de 'PopA' ")
    else:
       anos = 0

       while pop_A <= pop_B:
           anos+=1
           pop_A = pop_A + (pop_A * cres1 )
           pop_B = pop_B + (pop_B * cres2 )
    
       if cres1 >= cres2:        
          print ("A População 'A'' levou ",anos,"anos, para ultrapassar a População 'B'!")
         
    continuar = input(f"Deseja continuar?[S/N]")
    if continuar == 'Nn':
     break
     
     
           
       
        

