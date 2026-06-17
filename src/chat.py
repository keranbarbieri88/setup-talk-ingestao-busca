# Cria o loop no terminal para eu conversar com o sistema.
from search import search_prompt

def main():
    print("--- Bem-vindo ao Chat SuperTech ---")
    ask_function = search_prompt()

    if not ask_function:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    while True:
        pergunta = input("\nPERGUNTA: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break
        
        resposta = ask_function(pergunta)
        print(f"RESPOSTA: {resposta}")
        

if __name__ == "__main__":
    main()