# Média Móvel Simples

Esta função calcula a média móvel simples de um vetor dado uma determinada janela.

## Como Usar

*É necessário alterar o vetor e a janela diretamente no código*

```python
from seu_modulo import mediaMovelSimples

vetor_entrada = [1, 3, 5, 9, 21, 3, 9, 7]
tamanho_janela = 2
resultado = mediaMovelSimples(vetor_entrada, tamanho_janela)
print(resultado)
