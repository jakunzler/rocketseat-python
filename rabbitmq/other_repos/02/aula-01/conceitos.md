# Introdução
## O que são microsserviços?
"Microsserviços" são uma arquitetura de projeto, não algo específico de código ou nada do tipo.
Microsserviçoes são serviços independentemente implantáveis.

## Bounded Contexts
Em DDD, o conceito de bounded contexts se aplica como Linguagem Ubiqua, a linguagem de negócio/domínio
Algo pode ser o mesmo mas ter significados ou usos diferentes dependendo do contexto.

## A vantagem dos microsserviços
# Compartimentalização
Você pode moldar e usar cada serviço individualmente de acordo com sua necessidade, aumentando a eficiência e diminuindo a chance de problemas com serviços nem sendo usados
# Escalabilidade
Caso um serviço precise ser escalado, aumentar sua carga, ou outros casos, pode-se escalar apenas o serviço em questão, não precisando mudar nenhum dos outros.

## Quando são necessários
Quando se possui muitos serviços integrados e os fluxos do sistema acabam segurando a performance e criando problemas do tipo, onde a complexidade faz com que seja difícil executar e testar até ações simples, microsserviços podem ser a solução.
Em um exemplo com bancos de dados, cada serviço teria seu próprio banco, permitindo que mudanças à um serviço e seu banco não afetariam todos os outros serviços que fariam uso do mesmo banco.

## Tipos de conexões/mensagens
# HTTP
Conexões Rest normais, envio uma requisição http, se o serviço estiver offline, nada acontece.

## gRPC

## Async

## Message Broker
Envio uma mensagem através de um message broker (um serviço individual feito para transmitir mensagens entre outros serviços), onde ele recebe a mensagem a ser passada, e à salva.
O serviço que receberia a mensagem pede ao message broker e recebe a requisição inicial. Chamamos os dois serviços de Publisher e Consumer.
Exemplos de message brokers são Kafka ou RabbitMQ (que é o que vamos usar nesse projeto)

## Como um front-end se comunicaria com os serviços
# API Gateway
Uma aplicação ou serviço individual para fazer requisições aos microsserviços do back-end

## Distributed Tracing
Toda requisição tem um traceId, uma identificação daquela requisição/caminho, e o sistema de monitoramento pode, atráves dessa identificação, controlar e visualizar o funcionamento do sistema e possíveis problemas

## Pergunta: o que acontece se um banco de um serviço está offline?
Ou, como evitar que uma operação se repita caso haja problema com uma requisição?
Ela fica parada na fila do RabbitMQ, e só sai da fila quando resolvida com sucesso

## Como se implementa uma transação que depende de vários serviços ao mesmo tempo?
Se divide em microtransações (negócio gosta da palavra micro): Cada parte da comunição deve ser uma transação individual
# Exemplo
Uma requisição para ver se um usuário existe com propriedade x, primeiro se faz a transação de testar se o usuário existe; depois, se propriedade x está presente

## Circuit Breaker
Essencialmente, algo para evitar que um serviço seja sobrecarregado. Caso um serviço tenha tido n requisições falhadas, assumindo que ele está então com falhas ou sobrecarregado, ele impede qualquer outra requisição de ser feita à aquele serviço, impedindo que ele fique ainda mais sobrecarregado

## BFF
Back-end for Front-end
Uma técnica estilo GraphQL onde se pode fazer uma requisição para vários serviços ao mesmo tempo, o back-end sendo escrito especificamente para funcionar em volta do front-end

## E se o message broker cair?
Por isso nunca se deve hostear o message broker em apenas um lugar. Seguindo a mesma regra de backups, sempre deve existir um fallback caso o (nesse caso, um) message broker caísse.
