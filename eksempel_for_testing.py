# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:27:20 2021

@author: mohsenmohammadi
"""

def delelig(a, b):
    if a%b == 0:
        return True
    else:
        return False
    
    
#oppgave b
def perfekt(tall):
    sum_av_faktorer = 1
    for dele_på in range(2, (tall+2)//2):
        if delelig(tall, dele_på):
            sum_av_faktorer += dele_på
            print(f"Faktor: {dele_på}")
    print(f"sum av faktorer: {sum_av_faktorer}")
    if sum_av_faktorer == tall:
        return True
    else:
        return False
    
#oppgave c
if __name__ == "__main__":
    tall = int(input("which number do you want to chekck? "))
    if perfekt(tall):
        print(f"{tall} er perfekt")
    else:
        print(f"{tall} er ikke perfekt")
