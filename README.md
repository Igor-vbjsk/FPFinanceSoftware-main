# Software de Finanças (TCC)

Software de Finanças por proposta TCC

---

## Meta

Desenvolver um software de finanças pessoais capaz de auxiliar o usuário em suas atividades e decisões financeiras através de um ambiente visualmente acessível.

---

## TO-DO List

- [ ] Desenvolver a UI/UX do software

    - [ ] Desenvolver UX através dos dados obtidos via forms

        - [ ] Coletas dados suficientes para a tarefa

- [ ] Inserção das aplicações a interfaçe

    - [ ] Desenvolvimento das aplicações

        - [ ] Lista de Apps feitos mediante dados obtidos

- [ ] Correção de bugs

    - [ ] Alpha Testing com usuários fora do grupo

## Atribuições

| Tarefa | Atribuídos |
| ----------- | ----------- |
| Designer UI/UX | Joaopkl & Igão |
| Designer | Trojan |
| Desenvolvedor de aplicações | Igão |
| Gerenciamento | Fenrir |

---

## Referências 

| Name | Link |
| ----------- | ----------- |
| Simple Git Commands | https://www.atlassian.com/git/glossary#commands |
|Python UI Design Using Fret (Mobile) | https://www.youtube.com/watch?v=JJCjAUmNXBs |
| Python UI Design Using Tkinter (PC) | https://www.youtube.com/watch?v=mop6g-c5HEY |
| Python Financial application with Matplotlib | https://www.youtube.com/watch?v=wB9C0Mz9gSo |

--

#### 30-08-2024
- Criação base do software e sua estrutura interna de aplicação e UI

- A primeira criação base do software apresentou algumas dificuldades devido a melhor infraestrutura interna e melhores bibliotecas a serem usadas para um software de finanças, levando a decisão de ultilizar matplotlib para a aplicação na utilização de gráficos e outros elementos visuais, junto ao Tkinter para o desenvolvimento da interface gráfica. Outro problema em conta foi trabalhar os dois módulos em sincronia, o que levou a utilização de callbacks.


#### 04-09-2024
- Criação da GUI no Tkinter

- Processo foi relativamente simples, já que a lib é muito intuitiva. A principal dificuldade foi a organização do código, já que Python é mais focado na escrita estruturada e não orientado a objetos. Contudo, a criação da nossa 'base' foi finalizada, contendo: a janela principal como 'guia' para o que usuário quer fazer (reportar um novo gasto ou uma nova receita) e as janelas referentes aos gastos e receitas, ambas têm 2 campos: categorias e valor, sendo o primeiro referente a origem do gasto/ganho (como salário, retorno de investimentos, despesas fixas, emergências e etc) e o segundo referente à quantia de dinheiro. Nesse momento, o software têm apenas a GUI, que não faz integração com nenhuma API ou com o matplotlib, para validar que os botões estão funcionando de fato, ele retorna uma mensagem no terminal quando selecionado.

### 06/09/2024
- Aperfeiçoamente e etapa final da primeira aplicação;

- Após analise geral do codigo, recorremos a uma simplificação do mesmo criando classes e o dividindo em demais arquivos para melhor visualização e manutenção. O codigo até então, apresenta uma interface simples com o retorno de graficos individuais, para mostrar o porcentual de gastos e ganhos, separados por datas o qual foram inseridos os dados. De principio, já mostra a linhagem a qual iremos seguir, com um uso mais visual e intuitivo para o usario, voltando sempre dados precisos e de facil visualização. 
  
### 08/09/2024
- Correção de bugs e traduções;

- Durante o desenvolvimento das interfaçe e da coleta de dados para a inserção do mesmo aos gráficos, percebemos um problema recorrente na tentativa de inserir diferentes formatos de data para a análise, até descobrirmos que o módulo trabalhava com o formato ISO que, por padrão, se torna incoerente na expectativa de que o usuário o utilize ao invés do formato brasileiro ou americano. Por esse motivo, foi necessário a utilização de multiplos handlers para trabalhar com diferentes formados, incluindo principalmente o formato de data brasileiro, para que o usuário não enfrente dificuldades desnecessárias. Alguns problemas de tradução também foram corrigidos, permitindo que todo o software apresente uma interface brasileira.

### 12/09/2024
- Correção de escalas da aplicação

- As janelas da aplicação estavam saindo mal espaçadas, com botões sendo 'comidos' pela falta de tamanho da janela. O que foi feito foi aumentar o tamanho da janela inicial e mudanã da legenda "data de incidência" para apenas "data"

### 14/09/2024
- Remoção: Remoção do Software.py do nosso arquivo

- Sem mais utilidade, foi realizado a exclusão do nosso primeiro arquivo base, a fim de unificar o código em main.py.

### 01/11/2024
- Criacao da pasta em AppData

- Na intencao de armazenar localmente os dados entreges pelo usuario sem a utilizacao de SQL ou servidores, a criação de uma pasta em AppData/Local foi realizada para a inseção dos dados usuário em seu futuro uso após reabrir o software. 

### 04/11/2024
- Armazenamento de arquivos em AppData

- Para a utilização de arquivos de media como o icone do software e outras imagens, o software agora realiza o download online dos arquivos de media na pasta AppData do software para sua utilização enquanto o software estiver compilado.

### 07/11/2024
- Armazenamento adicional de dados em AppData e reformatação dos dados

- Na criação do armazenamento dos dados, as receitas e despesas apresentaram um desafio adicional no armazento do mesmos no arquivo em AppData/Local/NoVerde/data.txt, necessitando reformatar os dados dentro do arquivo para encaixar perfeitamente cada dado em sua respectiva formatação, tanto em dicionario quanto em lista. A forma de recoletar tal dados também foi alterada, utilizando um novo módulo para trabalhar com a diferença de formatação e assim inserindo cada dado em suas respectivas variáveis, possívelmente finalizando assim o processo de armazenamente e reutilização de dados no software.
