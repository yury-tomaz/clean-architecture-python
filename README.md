### Configuração do PYTHONPATH
Para garantir que o Python encontre os módulos corretamente, siga estes passos:

.1 Crie um arquivo `.env` no diretório raiz com o seguinte conteúdo:

```
    export PYTHONPATH="$PYTHONPATH:$PWD"
```

.2 Aplique a configuração:

```sh
    set -a
    source .env
```

### Executar Testes
Para garantir que o seu código esteja funcionando corretamente, você pode executar os testes automatizados usando o pytest. Siga estes passos:

.1 Certifique-se de que o ambiente virtual esteja ativado.

```sh
    source .venv/bin/activate
```

```sh
    pytest
```