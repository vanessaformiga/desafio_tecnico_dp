from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

faqs = [
    {"categoria": "Licença Maternidade", "pergunta": "Qual a duração da licença maternidade para servidoras públicas?", "resposta": "A licença maternidade é de 120 dias para servidoras públicas federais, podendo ser estendida em casos especiais como parto de múltiplos filhos ou saúde da mãe ou do bebê.", "fonte": "https://www.gov.br/servidor"},
    {"categoria": "Licença Paternidade", "pergunta": "Qual a duração da licença paternidade?", "resposta": "A licença paternidade é de 5 dias corridos para servidores públicos federais. Órgãos podem estender em situações específicas.", "fonte": "https://www.gov.br/servidor"},
    {"categoria": "Licença por Adoção", "pergunta": "Qual a duração da licença por adoção?", "resposta": "A licença por adoção é de 120 dias para adoção de crianças até 12 anos. Se houver mais de um adotante, regras podem variar.", "fonte": "https://www.gov.br/servidor"},
    {"categoria": "Licença Saúde", "pergunta": "Como solicitar afastamento por motivo de saúde?", "resposta": "O servidor deve apresentar atestado médico à chefia imediata e protocolar junto ao Departamento de Pessoal. Para afastamentos prolongados, perícia médica é obrigatória.", "fonte": "https://www.gov.br/esocial/pt-br"},
    {"categoria": "Licença para Capacitação", "pergunta": "Existe licença para estudo ou capacitação?", "resposta": "Sim, o servidor pode solicitar afastamento para cursos, capacitação ou pós-graduação, conforme regras do órgão e legislação vigente.", "fonte": "http://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm"},
    {"categoria": "Licença Prêmio", "pergunta": "O que é licença prêmio e quem tem direito?", "resposta": "Licença prêmio é concedida a servidores que completam determinado período de efetivo exercício, podendo variar conforme o órgão.", "fonte": "http://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm"},
    {"categoria": "Afastamento por Doença", "pergunta": "Qual procedimento para afastamento prolongado?", "resposta": "O servidor deve apresentar laudos médicos, passar por perícia e seguir os procedimentos do DP do órgão. O afastamento só é válido após aprovação da perícia.", "fonte": "https://www.gov.br/servidor"},
    {"categoria": "Licença para Tratar de Interesses Particulares", "pergunta": "O que é licença para tratar de interesses particulares?", "resposta": "É licença não remunerada concedida para assuntos pessoais, sem prejuízo do cargo, desde que solicitada e aprovada pelo órgão.", "fonte": "http://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm"},
    {"categoria": "Licença para Atividade Política", "pergunta": "O servidor pode se afastar para atividade política?", "resposta": "Sim, o servidor pode se afastar do cargo sem remuneração para exercer mandato eletivo ou atividade política regulamentada por lei.", "fonte": "http://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm"},
    {"categoria": "Afastamento por Acidente de Trabalho", "pergunta": "Como funciona o afastamento por acidente de trabalho?", "resposta": "O servidor acidentado deve apresentar laudo médico e comunicar o órgão competente. O afastamento será remunerado conforme legislação e perícia.", "fonte": "https://www.gov.br/servidor"},
    {"categoria": "Licença Capacitação Externa", "pergunta": "Posso me afastar para capacitação externa?", "resposta": "Sim, desde que a capacitação seja relevante para o cargo e autorizada pelo órgão, podendo ser remunerada ou não.", "fonte": "http://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm"},
    {"categoria": "Licença por Luto", "pergunta": "Qual a duração da licença por luto?", "resposta": "O servidor tem direito a até 8 dias consecutivos de licença remunerada em caso de falecimento de cônjuge, pais, filhos ou irmãos.", "fonte": "http://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm"},
    {"categoria": "Licença para Doação de Sangue", "pergunta": "Posso me afastar para doar sangue?", "resposta": "Sim, o servidor pode se ausentar por 1 dia a cada 12 meses para doar sangue, sem prejuízo da remuneração.", "fonte": "http://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm"},
    {"categoria": "Licença para Acompanhamento de Filho", "pergunta": "Existe licença para acompanhar filho doente?", "resposta": "Sim, o servidor pode solicitar afastamento em caso de doença do filho menor de idade, mediante atestado médico.", "fonte": "http://www.planalto.gov.br/ccivil_03/leis/l8112cons.htm"},
    {"categoria": "Licença Capacitação Interna", "pergunta": "Existe licença para capacitação interna no órgão?", "resposta": "Sim, o servidor pode participar de treinamentos internos ou cursos de aperfeiçoamento, com afastamento remunerado ou não, dependendo do regulamento do órgão.", "fonte": "https://www.gov.br/servidor"}
]

pdf_file = "faqs_licencas_completo.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

y = height - 50
for faq in faqs:
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Categoria: {faq['categoria']}")
    y -= 20
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Pergunta: {faq['pergunta']}")
    y -= 15
    c.drawString(50, y, f"Resposta: {faq['resposta']}")
    y -= 15
    c.drawString(50, y, f"Fonte: {faq['fonte']}")
    y -= 30
    if y < 100:
        c.showPage()
        y = height - 50

c.save()
print(f"PDF '{pdf_file}' criado com sucesso!")