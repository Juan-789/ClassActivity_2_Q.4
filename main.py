"""
Write a program that asks a user for a two digit integer. Swap its digits and print the output.
"""
digs = int(input("what numbers you want swapped "))
ones = digs%10
tens = digs //10
print (f"{ones}{tens}")
#Swap integers
