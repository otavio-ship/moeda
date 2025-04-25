from flask import Flask, render_template, request

app = Flask(__name__)

TAXAS = {
    'dolar': 5.10,  # 1 USD = 5.10 BRL
    'euro': 5.50  # 1 EUR = 5.50 BRL
}


@app.route('/', methods=['GET', 'POST'])
def converter_moeda():
    if request.method == 'POST':
        try:
            valor_reais = float(request.form.get('valor_reais'))
            moeda_destino = request.form.get('moeda_destino')

            if valor_reais <= 0:
                raise ValueError("O valor deve ser positivo")

            if moeda_destino not in TAXAS:
                raise ValueError("Moeda inválida")

            taxa = TAXAS[moeda_destino]
            valor_convertido = valor_reais / taxa

            return render_template('conversor.html',
                                   valor_reais=valor_reais,
                                   moeda_destino=moeda_destino,
                                   valor_convertido=round(valor_convertido, 2),
                                   taxa=taxa)

        except ValueError as e:
            erro = str(e) if str(e) else "Por favor, digite um valor válido"
            return render_template('conversor.html', erro=erro)

    return render_template('conversor.html')


if __name__ == '__main__':
    app.run(debug=True)