import pandas as pd
import re
# CARREGANDO O DATAFRAME
pokes_df = pd.read_csv(r'Training-stuff\pokemons\pokemon_data.csv')



print("\n======================================================")
print("Welcome to pokemon's world")
print("We have all the types of pokemons and their attributes")
print("======================================================\n\n")


# CHECANDO SE O USUÁRIO QUER CONTINUAR 
options = str(input("Would you like to see our categories? ")).lower()


# 
while options != 'yes' or options != 'y':
    
    
    # SE A RESPOSTA FOR SIM COM A STRING 'YES' OU PELO CHARACTER 'Y'

    if options == 'y' or options == 'yes':
        print("These are the options of categories we have for pokemons:\n")
        print("(A)1st Type\n(B)2nd Type\n(C)HP\n(D)Attack\n(E)Defense\n(F)Speed\n(G)Total Points\n(H)Number of legendaries\n(I)Number of megas\n")
        choose = str(input("Which one would you like to check: ")).lower()








        # SE A RESPOSTA FOR A OPÇÃO (A) --> TIPO 1

        if choose == 'a':

            print(pokes_df['Type 1'].value_counts())
            print(f'\nIn total we have: {pokes_df["Type 1"].value_counts().sum()} pokemons\n ')
            break








        # SE A RESPOSTA FOR A OPÇÃO (B) --> TIPO 2

        elif choose == 'b':

            print(pokes_df['Type 2'].value_counts())
            print(f'\nIn total we have: {pokes_df["Type 2"].value_counts().sum()} pokemons with a second type\n')
            break










        # SE A RESPOSTA FOR A OPÇÃO (C) --> HP

        elif choose == 'c':
            hl_hp = int(input("\nWould you like to see the 5 highest hp(hit points) pokemons or the lowest?\n(1) lowest (2) highest: "))

            # ENQUANTO A PESSOA NÃO ESCOLHER UMA DAS OPÇÕES DADAS (1 OU 2) ELA FICARÁ NO LOOP
            while hl_hp not in [1, 2]:

                # PEDIR NOVAMENTE A ENTRADA DA PESSOA
                hl_hp = int(input("Invalid input. Please choose 1 or 2: "))


            # CONDICIONAL IF SE A PESSOA QUISER POR ORDEM DO MAIOR HP OU MENOR
            if hl_hp == 1:
                # MENOR PARA O MAIOR
                print(pokes_df[['Name', 'HP']].sort_values(by=['HP', 'Name']).head(5))


            elif hl_hp == 2:
                # MAIOR PARA O MENOR
                print(pokes_df[['Name', 'HP']].sort_values(by=['HP', 'Name'], ascending=False).head(5))
            break












        # SE A RESPOSTA FOR OPÇÃO (D) --> ATTACK
        
        elif choose == 'd':
            hl_att = int(input("\nWould you like to check the 5 highest attack pokemons or the lowest?\n(1) lowest (2) highest: "))

            # ENQUANTO A PESSOA NÃO ESCOLHER UMA DAS OPÇÕES DADAS
            while hl_att not in [1, 2]:
                hl_att = int(input("Invalid input. Please choose 1 (highest attack) or 2 (lowest attack): "))

            

            if hl_att == 1:
                # MENOR PARA O MAIOR
                print(pokes_df[['Name', 'Attack']].sort_values(by=['Attack', 'Name']).head(5))



            elif hl_att == 2:
                # MAIOR PARA O MENOR
                print(pokes_df[['Name', 'Attack']].sort_values(by=['Attack', 'Name'], ascending=False).head(5))
            break













        # SE A RESPOSTA FOR OPÇÃO (E) --> DEFENSE

        elif choose == 'e':
            hl_def = int(input("\nWould you like to check the 5 most defensive pokemons or the lowest?\n(1) lowest (2) highest: "))

            # ENQUANTO A PESSOA NÃO ESCOLHER UMA DAS OPÇÕES DADAS
            while hl_def not in [1, 2]:
                hl_att = int(input("Invalid input. Please choose 1 (most defensive) or 2 (lowest defensive): "))

            

            if hl_def == 1:
                # MENOR PARA O MAIOR
                print(pokes_df[['Name', 'Defense']].sort_values(by=['Defense', 'Name']).head(5))



            elif hl_def == 2:
                # MAIOR PARA O MENOR
                print(pokes_df[['Name', 'Defense']].sort_values(by=['Defense', 'Name'], ascending=False).head(5))
            break

        














        # SE A RESPOSTA FOR OPÇÃO (F) --> SPEED

        elif choose == 'f':
            hl_speed = int(input("\nWould you like to check the 5 fastest pokemons or the lowest?\n(1) lowest (2) fastest: "))

            # ENQUANTO A PESSOA NÃO ESCOLHER UMA DAS OPÇÕES DADAS
            while hl_speed not in [1, 2]:
                hl_att = int(input("Invalid input. Please choose 1 (fastest) or 2 (lowest): "))

            

            if hl_speed == 1:
                # MENOR PARA O MAIOR
                print(pokes_df[['Name', 'Speed']].sort_values(by=['Speed', 'Name']).head(5))



            elif hl_speed == 2:
                # MAIOR PARA O MENOR
                print(pokes_df[['Name', 'Speed']].sort_values(by=['Speed', 'Name'], ascending=False).head(5))
            break

        













        # SE A RESPOSTA FOR OPÇÃO (G) --> TOTAL POINTS

        elif choose == 'g':
            hl_total = int(input("\nWould you like to check the 5 best pokemons or the worst?\n(1) worst (2) best: "))

            # ENQUANTO A PESSOA NÃO ESCOLHER UMA DAS OPÇÕES DADAS
            while hl_total not in [1, 2]:
                hl_att = int(input("Invalid input. Please choose 1 (best) or 2 (worst): "))

            

            if hl_total == 1:
                # MENOR PARA O MAIOR
                print(pokes_df[['Name', 'Total']].sort_values(by=['Total', 'Name']).head(5))



            elif hl_total == 2:
                # MAIOR PARA O MENOR
                print(pokes_df[['Name', 'Total']].sort_values(by=['Total', 'Name'], ascending=False).head(5))
            break
        













        # SE A RESPOSTA FOR OPÇÃO (H) --> LEGENDARIES

        elif choose == 'h':
            print("\nThese are the Legendaries found:")

            legendary_count = pokes_df.loc[pokes_df['Legendary'] == True, 'Legendary'].sum()
            print(pokes_df.loc[pokes_df['Legendary'] == True])
            print(f"In total we have {legendary_count} legendaries\n")
            break















        # SE A RESPOSTA FOR OPÇÃO (I) --> MEGAS

        elif choose == 'i':
            print("\nThese are the Megas found:")

            mega_pokes = pokes_df.loc[pokes_df['Name'].str.contains('Mega', flags=re.I, regex=True)]
            mega_count = len(mega_pokes)

            print(mega_pokes['Name'].head(10))
            print(f"\nIn total we have {mega_count} Megas\n")
            break











    elif options == 'no' or options == 'n':
        print("\nOk leaving...")
        break