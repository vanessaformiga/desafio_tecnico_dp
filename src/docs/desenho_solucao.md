``````

┌───────────────┐
│   Usuário     │
│ (Front-end)   │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   FastAPI     │
│  Backend API  │
│  Endpoints:   │
│  /login       │
│  /perguntas   │
│  /gerar-rel   │
│  /analise-pred│
└───────┬───────┘
        │
        │ Chamada de análise preditiva
        ▼
┌───────────────┐
│     LLM       │
│ (Ollama /     │
│ Hugging Face) │
│ - Recebe dados│
│ - Gera insights│
│ - Classifica risco│
└───────┬───────┘
        │
        │ Dados tabulares + insights
        ▼
┌───────────────┐
│ Análise       │
│ Preditiva +   │
│ Gráficos      │
│ Matplotlib /  │
│ Seaborn /     │
│ Plotly        │
└───────┬───────┘
        │
        │ JSON + base64 gráfico
        ▼
┌───────────────┐
│ Banco de Dados│
│ - PostgreSQL  │
│ - MySQL       │
│ Banco Vetorial│
│ - Pinecone  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│ Relatórios    │ 
│ + gráficos    │
└───────────────┘

``````