# documento html(lista.html)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>listagem</h1>
    <ul>
        {% for Transação in Transações %}
            <li>{{ Transação.descrição }} - {{ Transação.data }} - {{ Transação.valor }}</li>
        {% endfor %}
    </ul>            
</body>
</html>
