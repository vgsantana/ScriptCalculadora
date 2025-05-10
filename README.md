# ScriptCalculadora
Projeto realizado para cumprimento de modulo no curso de analista de dados da ebac, consiste em um script que executa uma calculadora desenvolvida em python, com o objetivo de testar os conhecimentos do modulo de python, linux e git.

# O código da calculadora
É um cóodigo simples que permite o usúario vizualizar um menu com as opcoes "Calcular" e "Sair", utilizando de numeros (1 ou 2) para escolher entre elas, caso escolha calcular, ele pode inserir dois numeros e depois escolher a operacao desejada para trabalhar com esses dois números.

# O script
O script é básicamente para executar o código, escrevi nele o caminho ate o arquivo .py e o executo dento do script, o importante é lembrar que pelo script ser um arquivo .sh, precisamos modificar as permissoes de usuário para poder executá-lo.

# Executando

Voce pode clonar esse repositorio para utilizar a calculadora. O primeiro passo é encontrar o local arquivo:

cd /home/usuario/ebac/linux/arquivo

criar o arquivo:

nano calculadora.sh

Caso tenha o codigo da calculadora pronto em um arquivo .py, basta escrever a seguindo instruicao no script:

python3 /caminho/ate/arquivo.py

Depois voce altera as permissoes para que o usuario possa executar o script e os outros apenas lê-lo

chmod 744 calculadora.sh

e por ultimo executar o script:

./calculadora.sh
