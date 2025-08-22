import matplotlib.pyplot as plt
import io
import base64

def gerar_grafico_base64(*, departamentos, valores, titulo):
    """
    Gera um gráfico de barras e retorna a imagem codificada em base64.
    
    Parâmetros:
    - departamentos: lista de nomes dos departamentos (eixo X)
    - valores: lista de valores correspondentes (eixo Y)
    - titulo: título do gráfico
    """
    import matplotlib.pyplot as plt
    import base64
    from io import BytesIO

    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(departamentos, valores, color='skyblue')
    ax.set_xlabel("Departamento")
    ax.set_ylabel("Valor")
    ax.set_title(titulo)
    ax.set_ylim(0,1)

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig)
    grafico_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return grafico_base64