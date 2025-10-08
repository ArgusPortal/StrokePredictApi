# StrokePredictApi

Descrição
---------
API REST para previsão de risco de AVC (stroke) baseada em um modelo de machine learning. Esta API recebe dados demográficos e clínicos do paciente e retorna uma estimativa do risco de AVC.

Principais funcionalidades
- Endpoint para prever risco a partir de uma entrada JSON.
- Validação simples dos dados recebidos.
- Estrutura pensada para fácil substituição do modelo de ML.

Tecnologias
-----------
- Node.js / .NET / Python (ajustar conforme a implementação do projeto)
- Biblioteca de ML (scikit-learn, TensorFlow, ONNX, etc.) — conforme modelo utilizado
- Docker (opcional)

Requisitos
----------
- Node.js >= 14.x ou runtime correspondente ao projeto
- Python 3.8+ (se aplicável)
- Docker (opcional)
- Dependências do projeto (ver package.json / requirements.txt)

Instalação
----------
1. Clone o repositório:
   git clone <repo-url>
2. Entre na pasta do projeto:
   cd StrokePredictionApi
3. Instale dependências:
   - Node: npm install
   - Python: pip install -r requirements.txt

Executando localmente
--------------------
- Node:
  npm start
  ou
  npm run dev

- Python (exemplo com Flask/FastAPI):
  uvicorn app.main:app --reload

- Docker:
  docker build -t strokepredictapi .
  docker run -p 8000:8000 strokepredictapi

Uso / Endpoints (exemplo)
-------------------------
- POST /predict
  - Descrição: Recebe um JSON com os atributos do paciente e retorna a probabilidade/risco de AVC.
  - Corpo (exemplo):
    {
      "age": 67,
      "hypertension": 0,
      "heart_disease": 1,
      "avg_glucose_level": 228.69,
      "bmi": 36.6,
      "smoking_status": "formerly smoked",
      "work_type": "Private",
      "gender": "Male",
      "ever_married": "Yes",
      "Residence_type": "Urban"
    }
  - Exemplo cURL:
    curl -X POST http://localhost:8000/predict \
      -H "Content-Type: application/json" \
      -d '{"age":67,"hypertension":0,"heart_disease":1,"avg_glucose_level":228.69,"bmi":36.6,"smoking_status":"formerly smoked","work_type":"Private","gender":"Male","ever_married":"Yes","Residence_type":"Urban"}'

Resposta (exemplo):
{
  "risk_score": 0.23,
  "prediction": "low",
  "threshold": 0.5
}

Validação e testes
------------------
- Adicione testes unitários para input validation e integração do endpoint /predict.
- Exemplos:
  - Testar entradas válidas e inválidas.
  - Testar integração com o modelo (mockar o modelo em testes unitários).

Boas práticas
------------
- Versionar o modelo de ML ou salvar um hash do arquivo do modelo.
- Logar previsões (sem dados sensíveis) para auditoria.
- Implementar testes e CI para garantir que mudanças não quebrem o serviço.

Contribuição
-----------
1. Abra uma issue descrevendo a mudança.
2. Crie um branch com a feature/fix.
3. Submeta um Pull Request com descrição e testes (quando aplicável).

Licença
-------
- Defina a licença do projeto (ex.: MIT) no arquivo LICENSE.

Contato
-------
- Para dúvidas sobre o projeto, abra uma issue no repositório.
