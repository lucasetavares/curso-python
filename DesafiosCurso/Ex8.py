# Faça um programa que leia um número inteiro
# e mostre na tela a sua tabuada.

n1 = int(input("Digite um valor para ver sua tabuada: "))
print(f'{n1} * 1 = {n1*1}')
print(f'{n1} * 2 = {n1*2}')
print(f'{n1} * 3 = {n1*3}')
print(f'{n1} * 4 = {n1*4}')
print(f'{n1} * 5 = {n1*5}')
print(f'{n1} * 6 = {n1*6}')
print(f'{n1} * 7 = {n1*7}')
print(f'{n1} * 8 = {n1*8}')
print(f'{n1} * 9 = {n1*9}')
print(f'{n1} * 10 = {n1*10}')
print('Ou: ')

for c in range(1,11):
    print(f'{n1} * {c} = {n1*c}')