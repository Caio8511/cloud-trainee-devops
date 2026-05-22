# SOC Defensive Automation Lab

## Descrição
Projeto de automação defensiva focado em Blue Team e SOC Operations utilizando Python.

## Funcionalidades
- Monitoramento de logs
- Detecção de brute force
- Registro de incidentes
- Bloqueio automático de IPs
- Alertas de segurança
- Simulação de resposta a incidentes

## Tecnologias utilizadas
- Python
- Log Analysis
- Defensive Security
- SOC Concepts
- Incident Response

## Estrutura

```bash
python-defense-tool/
├── log_monitor.py
├── security_logs.txt
├── alerts.txt
└── blocked_ips.txt

## Como executar o projeto

### 1. Entrar na pasta do projeto

```bash
cd python-defense-tool
```

---

### 2. Executar o monitor defensivo

```bash
python log_monitor.py
```

ou

```bash
python3 log_monitor.py
```

---

### 3. Simular ataque brute force

No arquivo `security_logs.txt`, adicione:

```text
Failed login from 192.168.1.50
Failed login from 192.168.1.50
Failed login from 192.168.1.50
```

---

### 4. Resultado esperado

O sistema irá:

- Detectar tentativas de brute force
- Gerar alertas automáticos
- Registrar incidentes
- Bloquear IPs suspeitos

Arquivos gerados automaticamente:

```bash
alerts.txt
blocked_ips.txt
```