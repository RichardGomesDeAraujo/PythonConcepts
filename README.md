<img src="Logo.png" align="Center" alt="Hands On Data" style="height: 100px; width:115px;"/>

<p>  <br>
  </p>
  
# Concepts, Application Fields and Libraries

<p>  <br>
  </p>

###### by [Richard Gomes de Araújo](https://github.com/RichardGomesDeAraujo) - 07/11/2023
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/RichardGomesDeAraujo)](https://github.com/RichardGomesDeAraujo)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/richardaraujoanalistadedados/)](https://www.linkedin.com/in/richardaraujoanalistadedados/)
[![Youtube Badge](https://img.shields.io/badge/-YouTube-ff0000?style=flat-square&labelColor=ff0000&logo=youtube&logoColor=white&link=https://www.youtube.com/channel/UCc_jlqHut_GkXc8ahgQHOOw)](https://www.youtube.com/channel/UCc_jlqHut_GkXc8ahgQHOOw)
<p>  <br>
  </p>
  
# Index
- [**Operadores Numéricos**](README.md#Operadores-Numéricos)
- [**Operadores de Comparação**](README.md#Operadores-de-Comparação)
- [**Operadores Lógicos**](README.md#Operadores-Lógicos)
- [**Tipos de Dados**](README.md#Tipos-de-Dados)
- [**Coleções de Dados**](README.md#Coleções-de-Dados)
- [**Variáveis**](README.md#Variáveis)
- [**Condicionais**](README.md#Condicionais)
- [**Looping**](README.md#Looping)
- [**Looping (while)**](README.md#Looping-(while))
- [**Comandos de Entrada**](README.md#Comandos-de-Entrada)
- [**Comandos de Saída**](README.md#Comandos-de-Saída)
- [**Importação de Arquivos**](README.md#Importação-de-Arquivos)
- [**Funções**](README.md#Funções)
- [**Classes**](README.md#Classes)
- [**Importação de Bibliotecas**](README.md#Importação-de-Bibliotecas)
- [**Tratamento de Erros e Exceções**](README.md#Tratamento-de-Erros-e-Exceções)
- [**Manipulação de Ambientes Virtuais**](README.md#Manipulação-de-Ambientes-Virtuais)

# Application Fields and Libraries:
- [**Análise de Dados e AI (Artificial Intelligence)**](README.md#Análise-de-Dados-e-AI-(Artificial-Intelligence))
- [**Automação WEB/Scraping**](README.md#Automação-WEB/Scraping)
- [**Automação de Tarefas**](README.md#Automação-de-Tarefas)
- [**Desenvolvimento Web**](README.md#Desenvolvimento-Web)
- [**Desenvolvimento APP**](README.md#Desenvolvimento-APP)
- [**Desenvolvimento Games**](README.md#Desenvolvimento-Games)

# Python Commands:
- [**terminal**](README.md#terminal)
- [**type**](README.md#type)
- [**range**](README.md#range)
- [**input**](README.md#input)
- [**len**](README.md#len)
- [**loop**](README.md#loop)
## String Commands
- [**isalnum**](README.md#isalnum)
- [**capitalize**](README.md#capitalize)
- [**string find**](README.md#string-find)
- [**string center**](README.md#string-center)
## List Commnands
- [**list append**](README.md#list-append)
- [**list sort**](README.md#list-sort)
  
---

### Operadores Numéricos
Visualization using SQL commands:
```python
+ Adição
- Subtração
* Multiplicação
/ Divisão
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Operadores de Comparação
```python
> Maior
< Menor
>= Maior e Igual
<= Menor e Igual
== Igual
= Recebe Valor
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Operadores Lógicos
```python
4 > 3 and 4 >= 2 
5 < 6 or 4 <= 3 
not 6 < 5
cicms not in 'SN'
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Tipos de Dados
```python
“tipo de dado” = string 
40 = int 
2.0 = float 
True/False = bool 
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Coleções de Dados
```python
Listas = [a, b, c] 
Dicionários = {“chicará”, “pires”, “colher”} 
Tuplas = (10, 20, 30) 
Conjuntos = set([10, 20, 30])
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Variáveis
```python
Variável = 100 
Variável = Variável * 100 
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Condicionais
```python
if anexo == 6:
  impostos = 30
  break
else:
  print('\033[33mOpção Inválida! Por favor, digite novamente.\033[m')
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Looping
```python
for i in range(10): 
variavel = variavel + 5 
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Looping (while)
```python
while vc == 0:
    try:
        vc = float(input('Digite o Valor de Compra do Produto: R$ '))
    except:
        print('\033[33mValor Incorreto! Por favor, informe o valor correto\033[m')
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Comandos de Entrada
```python
vc = float(input('Digite o Valor de Compra do Produto: R$ '))
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Comandos de Saída
```python
print(f'\033[37mValor de Venda: R$ {vv:.2f}')
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Importação de Arquivos
```python
with open(“C:/documentos/arquivo.txt”, “w”) as arquivo: 
texto = “Cotações” 
arquivo.write(texto) 
arquivo.close() 
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Funções
```python
def primeira_funcao(): 
print(“Primeira Função”)
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Classes
```python
def__init__(self, nome, idade): 
self.nome = nome 
self.idade = idade 
def funcao(self): 
print(“Meu nome é”, self.nome) 
print(“Minha idade é”, self.idade)
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Importação de Bibliotecas
```python
from Biblioteca import Função
import Pandas as pd
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Tratamento de Erros e Exceções
```python
for i in range(10): 
try: 
     #comandos 
except:
     print(“Erro de Digitação”) 
     continue 
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Manipulação de Ambientes Virtuais
```python
Microsoft Windows [versão 10.0.22000.795] 
© Microsoft Corporation. Todos os direitos reservados.  

C:\Users\Documentos>conda create –n MeuAmbienteVirtual python=3.6 pip
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>
  
---

# Application Fields and Libraries

### Análise de Dados e AI (Artificial Intelligence)
```python
Numpy 
Pandas 
Matplotlib 
Seaborn 
Scikitlearn 
TensorFlow 
Keras 
Pytorch 
Theano 
MxNet 
Caffe 
CNTK 
Pillow
OpenCv 
ApacheSpark 
Hadoop
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Automação WEB/Scraping
```python
Urllib 
Requests 
Selenium 
Webbot 
Beautifulsoup 
Scrapy 
PyAutoGUI 
Keyboard 
Pynput 
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Automação de Tarefas
```python
OS 
RPA 
APSScheduler 
Watchdog 
Paramiko 
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Desenvolvimento Web
```python
Django 
Flask 
CherryPy 
Pyramid 
TurboGears 
Web2py 
Bottle 
Tornado	 
Falcon 
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Desenvolvimento APP
```python
Kivy 
BeeWare 
Python-for-Android 
PyJNlus 
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

### Desenvolvimento Games 
```python
Pygame 
PyKyra 
Pyglet 
Arcade 
PyOpenGl 
Panda3D 
Ren’Py 
Cocos2d
```
###### [⏪](README.md#Index)
<p>  <br>
  </p>

# Python Commands
### terminal
Commands used in terminal:
```python
# create a virtual machine
python -m venv venv

# Activate the virtual machine
.\venv\Scripts\activate

# to execute scripts
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>

### type
Return the type of the data:
```python
# input
x = 10
print(type(x))

# output
<class 'int'>
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>  

### range
Return a range from the data:
```python
# Example 1
# input
x = range(3)
for n in x:
  print(n)

# output
0
1
2

# Example 2
# input
x = range(3, 6)
for n in x:
  print(n)

# output
3
4
5

# Example 3
# input
x = remge(3,8,2)
for n in x:
  print(n)

# output
3
5
7
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>  

### input
Command to input some value in the code:
```python
print("Enter your name: ")
x = input()
print("Hello, " + x)

```

###### [⏪](README.md#Index)
<p>  <br>
  </p>  

### len
Show the length of the string:
```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>  

### loop
Commnand used to create a loop in the code:
```python
# Example 1
# loop in a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
 # output
apple
banana
cherry

# Example 2
# loop through a string
for x in "cherry"
 print(x)

# output
c
h
e
r
r
y

```

###### [⏪](README.md#Index)
<p>  <br>
  </p>

## String Commands
### isalnum
Return if the string is alphanumeric or not:
```python
# input
txt = "Company12"
x = txt.isalnum()
print(x)

# output
True
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>

### capitalize
Returns a string where the first character is upper case:
```python
# input
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

# output
Hello, and welcome to my wolrd."
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>  

### string find
Return the first occurrence of the specified value:
```python
# input
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# output
7
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>

### string center
Return the string in a center between the specific number of strings:
```python
# imput
txt = "banana"
x = txt.center(20)
print(x)

# output
       banana       
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>  

## List Commands
### list append
Add value in a list:
```python
# input
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# output
['apple', 'banana', 'cherry', 'orange']
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>

### list sort
Return the values in a specific order:
```python
# Example 1
# imput
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# output
['BMW', 'Ford', 'Volvo']

# Example 2
# input
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

# output
['Volvo', 'Ford', 'BMW']
```

###### [⏪](README.md#Index)
<p>  <br>
  </p>  
  

  
