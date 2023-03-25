# -*- coding: utf-8 -*-
anoatual=int(input('Ano Atual: '))
idadeatual=int(input('Idade Atual: '))
outroano=int(input('Outro ano: '))
nome=input('Nome: ')
idade=int(idadeatual + outroano - anoatual)
print(nome, ',' 'no ano de',outroano, 'você terá', idade, 'anos')