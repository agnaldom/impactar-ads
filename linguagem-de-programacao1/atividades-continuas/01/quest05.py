#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Faça um programa que pergunte quanto você ganha por hora 
#  e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
gph = float(input("Digite o valor ganho por hora: "))
ntm = float(input("Digite o numero de hora trabalhas no mes: "))

totalSalario = gph * ntm

print("O seu salario eh: ", totalSalario)
