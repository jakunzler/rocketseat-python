# rocketseat-python-rabbitmq
Project for following the lessons about RabbitMQ integration on Python

# dotenv:

Execute: 
`cp .env-example .env`

Go to BotFather telegram bot and get the bot token, update the token on .env file.

Go to [[https://api.telegram.org/bot<TOKEN>/getUpdates]], then add the bot to a channel and use the chat_id to update the field on .env file.

## Starting rabbitmq_management
`sudo rabbitmq-plugins enable rabbitmq_management`

## URL to access it
http://localhost:15672/#/


## from [[https://ipv6.rs/tutorial/POP!_OS_Latest/RabbitMQ/]]

### Start RabbitMQ and Enable it on Boot

After installing RabbitMQ, start the RabbitMQ service by running the following command.

`sudo systemctl start rabbitmq-server`

To enable the RabbitMQ service to start automatically on boot, run the following command.

`sudo systemctl enable rabbitmq-server`

### Check RabbitMQ Status

After starting RabbitMQ, we can check the status of RabbitMQ by running the following command.

`sudo systemctl status rabbitmq-server`
