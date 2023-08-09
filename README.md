<h1>🐍MUNDO 00 🐍<h1>
️<h3>⚠️ O objetivo dessa Mochila e armazenar conhecimentos e usar para futuros exemplos voltados a codigos orientado a objetos com um exemplo de uma conta bancaria!⚠️<h3>
  
<h5>📜 O codigo define uma classe chamada Conta, que representa uma conta bancária com vários métodos para gerenciar e manipular informações da conta. Vou resumir os principais componentes e funcionalidades da classe:
<br>
<br>
 <br>
🔧 Atributos (Propriedades):
<br>
🔒__numero: Número da conta (privado).
  <br>
🔒__titular: Nome do titular da conta (privado).
  <br>
🔒__saldo: Saldo atual da conta (privado).
  <br>
🔒__limite: Limite de cheque especial (privado).
  <br>
  <br>
<br>
 <br>
  <br>
<br>
  
🔧 Inicializador (__init__):
<br>
Inicializa a conta com os valores fornecidos para numero, titular, saldo e limite.
<br>
<br>
   <br>
  <br>
<br>
🔧 Métodos:
<br>
<br>
extrato(): Imprime o saldo da conta e o nome do titular.
<br>
  <br>
deposita(valor): Adiciona o valor ao saldo da conta.
<br>
  <br>
pode_sacar(valor_a_sacar): Verifica se é possível realizar um saque de valor_a_sacar considerando o saldo da conta e o limite de cheque especial.
<br>
  <br>
saca(valor): Realiza um saque de valor da conta se o saque for permitido.
<br>
  <br>
transfere(valor, destino): Transfere valor da conta para outra conta (destino).
<br>
  <br>
pagamento(valor, destino): Deposita valor em outra conta (destino) como um pagamento.
<br>
  <br>
get_saldo(): Retorna o saldo atual da conta.
<br>
  <br>
get_titular(): Retorna o nome do titular da conta.
<br>
  <br>
limite: Uma propriedade que retorna o limite de cheque especial.
<br>
  <br>
limite(limite): Um definidor que atualiza o limite de cheque especial.
<br>
  <br>
Método Estático (codigos_bancos):
<br>
  <br>
Um método estático que retorna um dicionário de códigos de bancos.
   <br>
  <br>
  
📜 A classe encapsula as informações e operações da conta usando princípios de programação orientada a objetos. Ela garante a encapsulação dos dados usando atributos privados e fornece métodos para interagir com a conta, como depósitos, saques, transferências e verificação de saldo. As propriedades limite e get_saldo oferecem acesso controlado a esses atributos.
 <br>
  <br>
📜 O método estático codigos_bancos fornece informações relacionadas a códigos de bancos, mas não interage com dados específicos da instância, demonstrando o uso cuidadoso de métodos estáticos em um contexto orientado a objetos.
 <br>
  <br>
📜 O código demonstra princípios de encapsulamento, abstração e polimorfismo, que são centrais para a programação orientada a objetos. Vale ressaltar que, embora o código fornecido seja um exemplo funcional, existem alguns erros de digitação e problemas de estilo que podem ser corrigidos para maior clareza e consistência.<h5>
