"""
Estruturas condicionais
if (Se), else, elif (else if)
"""

"""
#estrutura condicional if, else if, else em C

if(idade < 18) {
    printf("Menor de idade);
}else if(idade == 18){
    printf("Tem 18 anos);
}else{
    printf("É maior de idade")
}
"""

"""
#estrutura condicional if, else if, else em Java

if(idade < 18) {
    system.out.println("Menor de idade);
}else if(idade == 18){
   system.out.println("Tem 18 anos")
}else{
    system.out.println("É maior de idade")
}
"""
idade = 18
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')
