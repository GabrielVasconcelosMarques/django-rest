# django-rest

--- 

## Sobre
- Aplicação desenvolvida como backend de uma aplicação, seu objetivo é consultar no site da [Drogasil](https://www.drogasil.com.br) e trazer os resultados da primeira página, relacionado ao produto ou sintoma que o usuário solicitou
- Esta aplicação foi desenvolvida utilizando o ambiente virtual do python, o framework ```django rest```, a biblioteca ```beautifulsoup``` e a biblioteca ```requests```
- Desenvolvida no sistema operacional windows
- Nesta aplicação, eu faço a requisição dos dados referentes a pesquisa, e resolvi retornar todos eles separados numa lista para cada, onde para cada produto, obtive o nome do mesmo, preço e restrição de tarja para compra daquele produto, sendo retornado todos os dados em json.


## Instruções de execução
Você deverá realizar o clone deste projeto na sua área de trabalho:
- Navegando pelo terminal do seu sistema operacional, vá até a pasta da sua área de trabalho e digite o comando ```git clone https://github.com/GabrielVasconcelosMarques/django-rest.git```

Após ter feito o clone do projeto, abra a pasta do projeto na IDE de sua escolha:
- Como o projeto foi desenvolvido num ambiente virtual do python, você deverá ativar o ambiente, antes de executá-lo, rodando o seguinte comando: 
- Caso esteja no windows: ```.\venv\Scripts\activate```, caso apresente algum erro nessa ativação, no windows, digite o comando ```Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned``` e após isso, digite novamente o comando ```.\venv\Scripts\activate```
- Caso esteja no linux: ```source bin/activate```
- Após rodar o comando acima, você deverá instalar as bibliotecas que foram utilizadas para essa aplicação, elas estão descritas no arquivo requirements.txt deste repositório. Para instalá-los, você deverá utilizar o comando ```pip install -r requirements.txt```
- Se por alguma razão o comando acima não funcionar, dentro do seu ambiente, você digita os comandos de instalação ```pip install django```, ```pip install beautifulsoup4``` e ```pip install requests```.

Agora, para executar a aplicação:
- Na pasta raiz do projeto, pela sua IDE, digite o comando ```python .\manage.py runserver```, caso esteja no windows
- Caso esteja no linux, digite o comando ```python3 manage.py runserver```
- Abra no seu navegador, o endereço ```http://127.0.0.1:8000/produtos/<nome_produto_ou_sintoma>```

## Utilização da aplicação
- Após a aplicação estar rodando, você vpoderá alterar na barra de endereço do navegador, mudando sempre após /produtos, inserindo qual produto ou sintoma deseja pesquisar, sendo retornado um json, contendo para cada produtos uma lista, tendo em cada lista o nome do produto, valor dele e sua restrição de tarja para compra.


## Demonstração do projeto

### Mostrando tela com retorno para o produto desodorante
![1](https://user-images.githubusercontent.com/66792384/192760456-5137c8d4-d417-4a39-bbe8-afe0284cfed7.PNG)

### Mostrando tela com retorno para o sintoma de gripe
![2](https://user-images.githubusercontent.com/66792384/192760463-dc0704ac-f4a6-4350-b2a8-9c3d45768e7e.PNG)

### Mostrando tela com retorno para produtos que contenham espaçamento no seu nome, como no exemplo abaixo lenço umedecido
![3](https://user-images.githubusercontent.com/66792384/192760465-217be3b1-a178-4840-a5ff-d8979c5db3f2.PNG)

### Mostrando tela caso o retorno seja apenas de um produto
![4](https://user-images.githubusercontent.com/66792384/192760467-9d1e7971-e990-4d4e-a662-6bab1cfae9be.PNG)

### Mostrando requisições realizadas pelo Postman, uma aplicativo que realiza requisições em api's e mostra seu retorno
![5](https://user-images.githubusercontent.com/66792384/192758114-18fa3100-4396-4997-97b9-7ad6984725db.PNG)

## Author
### Gabriel Vasconcelos
