import string

class TextCrypto:
    def __init__(self):
        self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
    
    def caesar_encrypt(self, text: str, shift: int) -> str:
        """Criptografa o texto usando cifra de César."""
        result = ""
        for char in text:
            if char in self.alphabet:
                index = (self.alphabet.index(char) + shift) % len(self.alphabet)
                result += self.alphabet[index]
            else:
                result += char
        return result
    
    def caesar_decrypt(self, text: str, shift: int) -> str:
        """Descriptografa o texto usando cifra de César."""
        return self.caesar_encrypt(text, -shift)
    
    def xor_crypt(self, text: str, key: str) -> str:
        """Criptografa/Descriptografa usando XOR (a mesma função serve para ambos)."""
        result = ""
        key_length = len(key)
        for i, char in enumerate(text):
            key_char = key[i % key_length]
            result += chr(ord(char) ^ ord(key_char))
        return result

def main():
    crypto = TextCrypto()
    
    while True:
        print("\n=== Sistema de Criptografia ===")
        print("1. Cifra de César")
        print("2. Criptografia XOR")
        print("3. Sair")
        
        choice = input("\nEscolha uma opção (1-3): ")
        
        if choice == "3":
            print("Obrigado por usar o sistema!")
            break
            
        if choice == "1":
            text = input("Digite o texto: ")
            try:
                shift = int(input("Digite o deslocamento (número inteiro): "))
                print("\n1. Criptografar")
                print("2. Descriptografar")
                op = input("Escolha a operação (1-2): ")
                
                if op == "1":
                    result = crypto.caesar_encrypt(text, shift)
                    print(f"\nTexto criptografado: {result}")
                elif op == "2":
                    result = crypto.caesar_decrypt(text, shift)
                    print(f"\nTexto descriptografado: {result}")
                    
            except ValueError:
                print("Erro: O deslocamento deve ser um número inteiro!")
                
        elif choice == "2":
            text = input("Digite o texto: ")
            key = input("Digite a chave: ")
            if key:
                result = crypto.xor_crypt(text, key)
                print(f"\nResultado (mesma função para criptografar/descriptografar): {result}")
            else:
                print("Erro: A chave não pode estar vazia!")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
