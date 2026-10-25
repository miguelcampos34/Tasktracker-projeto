# TaskTracker 
Sistema de Interface de Linha de Comando (CLI) para gerenciamento de tarefas, desenvolvido como parte da Fase 2 do Bootcamp II.

## Funcionalidades
- **Cadastro de tarefas** com validação estrita de dados (títulos não vazios e prioridades predefinidas).
- **Classificação por prioridade** (Alta, Média, Baixa).
- **Visualização rápida** da lista de pendências.
- **Conclusão de tarefas**, permitindo atualizar dinamicamente o status das atividades para "Concluída".
- **Armazenamento persistente**, salvando automaticamente todas as tarefas em um arquivo `tarefas.json` local para não perder os dados ao fechar a aplicação.

## Tecnologias Utilizadas
- Python 3
- Módulo `json` e `os` (Biblioteca Padrão do Python)

##  Como Executar com Docker
Certifique-se de que tem o Docker e o Docker Compose instalados.

1. Clone o repositório e aceda à pasta raiz do projeto.
2. Construa a imagem e inicie o contentor em modo interativo executando:
   `docker-compose run --build tasktracker-app`
3. O menu do TaskTracker aparecerá automaticamente no seu terminal.
