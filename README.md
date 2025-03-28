# 🔐 Sistema de Criptografia e Descriptografia

Um sistema Python que implementa dois métodos populares de criptografia: Cifra de César e Criptografia XOR. Este projeto foi criado com fins educacionais para demonstrar conceitos básicos de criptografia.

## ⭐ Demonstração
![Sistema de Criptografia](https://img.shields.io/badge/Python-Criptografia-blue)
- Cifra de César: Método clássico de substituição
- Criptografia XOR: Método moderno e reversível

## 📋 Índice
- [Funcionalidades](#funcionalidades)
- [Métodos de Criptografia](#métodos-de-criptografia)
- [Como Usar](#como-usar)
- [Exemplos](#exemplos)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Segurança](#segurança)

## ✨ Funcionalidades
- Interface de linha de comando interativa
- Dois métodos de criptografia diferentes
- Suporte para letras, números e caracteres especiais
- Fácil de usar e entender

## 🔑 Métodos de Criptografia

### 1. Cifra de César
- Um método clássico de criptografia por substituição
- Cada letra é deslocada um número fixo de posições no alfabeto
- **Exemplo:**
  - Texto: "ABC", Deslocamento: 1
  - Resultado: "BCD"
- Para descriptografar, use o mesmo número de deslocamento em sentido contrário

### 2. Criptografia XOR
- Usa operação XOR bit a bit entre o texto e a chave
- A mesma operação serve para criptografar e descriptografar
- **Exemplo:**
  - Texto: "Hello"
  - Chave: "key"
  - A chave é repetida se necessário: "keyke"
  - Cada caractere é combinado com o caractere correspondente da chave

## 🚀 Como Usar

1. Execute o programa:
```bash
python crypto_app.py
```

2. Escolha um método de criptografia:
```
=== Sistema de Criptografia ===
1. Cifra de César
2. Criptografia XOR
3. Sair
```

3. Siga as instruções na tela para:
   - Digite seu texto
   - Forneça a chave ou deslocamento
   - Escolha entre criptografar ou descriptografar

## 💡 Exemplos

### Cifra de César
```
Texto original: "Hello"
Deslocamento: 3
Texto criptografado: "Khoor"
```

### XOR
```
Texto original: "Secret"
Chave: "key"
Texto criptografado: [resultado em caracteres especiais]
```

## ⚙️ Requisitos
- Python 3.6 ou superior
- Não necessita bibliotecas externas

## 📥 Instalação
1. Clone o repositório:
```bash
git clone [URL_DO_SEU_REPOSITORIO]
```

2. Entre na pasta do projeto:
```bash
cd CriptografiaDescriptografia
```

3. Execute o programa:
```bash
python crypto_app.py
```

## 🔒 Segurança
**Nota Importante:** Este projeto é para fins educacionais. Para dados sensíveis em ambiente de produção, use bibliotecas de criptografia estabelecidas e seguras como:
- PyCrypto
- cryptography
- PyNaCl

## 👨‍💻 Autor
[Seu Nome]

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
