# 📌 Boas Práticas com Git e GitHub

Guia de boas práticas essenciais para manter o projeto organizado, seguro e colaborativo.

---

## 🎯 Pilares Principais

1. **Organização e versionamento de código**
   - Manter o histórico do projeto limpo, estruturado e compreensível a cada alteração.
   - Manter arquivos temporários ou desnecessários fora do versionamento (como pastas de cache `__pycache__`).

2. **Colaboração entre desenvolvedores**
   - Trabalhar com branches dedicadas para novas funcionalidades (`feature/...`) ou correções (`fix/...`), evitando alterações diretas na branch principal (`main`).
   - Facilitar o trabalho em equipe sem conflitos de código.

3. **Controle de versões e rastreabilidade**
   - Permitir identificar e reverter problemas rapidamente caso surjam bugs em versões posteriores.
   - Possibilitar restaurar versões anteriores estáveis com segurança.

---

## 💡 Dicas para o dia a dia

- **Commits pequenos e objetivos:** Faça commits com frequência, focados em uma única alteração.
- **Mensagens descritivas:** Use mensagens claras no commit explicando o que foi feito (ex: `git commit -m "Corrige divisão por zero"`).
- **Sincronização:** Sempre dê `git pull` antes de começar a trabalhar para garantir que está com o código mais recente.

