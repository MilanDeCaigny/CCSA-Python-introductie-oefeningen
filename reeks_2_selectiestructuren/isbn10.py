input1 = int(input())
input2 = int(input())
input3 = int(input())
input4 = int(input())
input5 = int(input())
input6 = int(input())
input7 = int(input())
input8 = int(input())
input9 = int(input())
input10 = int(input())

controle = (input1 + 2*input2 + 3*input3 + 4*input4 + 5*input5 + 6*input6 + 7*input7 + 8*input8 + 9*input9) % 11

if input10 == controle:
     print("OK")
else:
     print("FOUT")