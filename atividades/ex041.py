from datetime import date
NascAtleta = int(input('Qual o ano de nascimento do atleta?\n'))
idadeAtleta = date.today().year - NascAtleta
if idadeAtleta <= 9 :
    print('Esse atleta deve estar na categoria \033[1;36mMirim\033[m')
elif idadeAtleta <= 14 :
    print('Esse atleta deve estar na categoria \033[1;35mInfantil\033[m')
elif idadeAtleta <= 19 :
    print('Esse atleta deve estar na categoria \033[1;32mJunior\033[m')
elif idadeAtleta == 20 :
    print('Esse atleta deve estar na categoria \033[1;33mSênior\033[m')
else :
    print('Esse atleta deve estar na categoria \033[1;31mMaster\033[m')
