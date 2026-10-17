import json
import os

ARQUIVO_DADOS = 'tarefas.json'

def carregar_tarefas():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def exibir_menu():
    print("\n" + "="*30)
    print("      TASKTRACKER MENU")
    print("="*30)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Concluir uma tarefa")
    print("4. Sair da aplicação")
    print("="*30)

def cadastrar_tarefa(tarefas):
    print("\n--- Nova Tarefa ---")
    
    while True:
        titulo = input("Título da tarefa (obrigatório): ").strip()
        if titulo:
            break
        print("Erro: O título é obrigatório e não pode ficar em branco. Tente novamente.")
    
    descricao = input("Descrição (opcional): ").strip()
    
    while True:
        prioridade = input("Prioridade (Alta, Média, Baixa): ").strip().capitalize()
        if prioridade in ["Alta", "Média", "Media", "Baixa"]:
            if prioridade == "Media": prioridade = "Média"
            break
        print("Erro: Prioridade inválida. Digite estritamente Alta, Média ou Baixa.")
    
    data_limite = input("Data Limite (DD/MM/AAAA ou formato livre): ").strip()
    
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    tarefas.append(tarefa)
    salvar_tarefas(tarefas) 
    print("\nTarefa adicionada com sucesso!")
    input("\nPressione Enter para voltar ao menu...")

def visualizar_tarefas(tarefas):
    print("\n--- Minhas Tarefas ---")
    
    if not tarefas:
        print("\nVocê não tem nenhuma tarefa pendente no momento. Aproveite o seu dia!")
        input("\nPressione Enter para voltar ao menu...")
        return

    for i, t in enumerate(tarefas, 1):
        print(f"\n[{i}] {t['titulo']}")
        print(f"    Descrição: {t['descricao'] if t['descricao'] else 'Nenhuma'}")
        print(f"    Prioridade: {t['prioridade']}")
        print(f"    Data Limite: {t['data_limite'] if t['data_limite'] else 'Não definida'}")
        print(f"    Status: {t['status']}")
        
    input("\nPressione Enter para voltar ao menu...")

def concluir_tarefa(tarefas):
    print("\n--- Concluir Tarefa ---")
    
    if not tarefas:
        print("\nVocê não tem nenhuma tarefa registrada no momento.")
        input("\nPressione Enter para voltar ao menu...")
        return
        
    for i, t in enumerate(tarefas, 1):
        print(f"[{i}] {t['titulo']} (Status atual: {t['status']})")
        
    try:
        indice = int(input("\nDigite o número da tarefa que deseja concluir (ou 0 para cancelar): "))
        
        if indice == 0:
            return
            
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]["status"] = "Concluída"
            salvar_tarefas(tarefas) 
            print("\nTarefa marcada como concluída com sucesso!")
        else:
            print("\nErro: Número de tarefa inválido.")
            
    except ValueError:
        print("\nErro: Por favor, introduza um número válido.")
        
    input("\nPressione Enter para voltar ao menu...")

def main():
    tarefas = carregar_tarefas()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            print("\nSaindo do TaskTracker... Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")
            input("\nPressione Enter para tentar novamente...")

if __name__ == "__main__":
    main()
