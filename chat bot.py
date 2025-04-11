def simple_chatbot():
    print("Olá! Sou seu chatbot. Digite 'sair' para encerrar.")
    
    # Dicionário de respostas
    responses = {
        "oi": "Olá! Como posso ajudar?",
        "como vai": "Estou bem, obrigado por perguntar!",
        "qual é o seu nome": "Meu nome é PyBot.",
        "o que você faz": "Eu sou um chatbot simples criado em Python.",
        "tchau": "Até logo! Foi bom conversar com você."
    }
    
    while True:
        user_input = input("Você: ").lower()
        
        if user_input == "sair":
            print("Chatbot: Até a próxima!")
            break
        
        # Verificar se a pergunta está no dicionário
        for key in responses:
            if key in user_input:
                print(f"Chatbot: {responses[key]}")
                break
        else:
            print("Chatbot: Desculpe, não entendi. Pode reformular?")

if __name__ == "__main__":
    simple_chatbot()