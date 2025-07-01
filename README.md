# 🥁 Bateria Virtual com Visão Computacional

Um simulador de bateria interativo que usa visão computacional (OpenCV) para detectar movimentos e reproduzir sons de bateria através do Pygame. O projeto é otimizado para uso com uma câmera posicionada no estilo zênite (vista de cima).

## 🎯 Recursos

- Detecção de movimento em tempo real usando OpenCV
- Interface gráfica com Pygame
- Sons realistas de bateria
- Fácil configuração e personalização
- Gerenciamento de dependências com `uv` (ultra-rápido!)

## 📋 Pré-requisitos

- Python 3.12+
- Câmera web
- `uv` instalado (gerenciador de pacotes Python)

## 🚀 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Miguel-Oliveiraa/python-drums-master.git
   cd python-drums
   ```

2. Instale as dependências com `uv`:
   ```bash
   uv sync
   ```

## ▶️ Como usar

1. Posicione sua câmera no estilo zênite (vista de cima) apontando para a área de toque
2. Execute o programa:
   ```bash
   python main.py
   ```
3. Ajuste a janela da câmera para enquadrar sua área de toque
4. Use as mãos ou baquetas para tocar os componentes da bateria virtual

## 🎛️ Controles

- **Toque na tela**: Tocar os componentes da bateria
- **Tecla 'q'**: Sair do programa
- **Tecla 'r'**: Redefinir calibração

## 🛠️ Estrutura do Projeto

```
python-drums/
├── main.py            # Ponto de entrada principal
├── README.md          # Este arquivo
├── requirements.txt   # Dependências do projeto
└── playground/        # Códigos experimentais
    ├── virtual_drums.py
    └── drum_kit.py
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
