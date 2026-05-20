import streamlit as st
import json
import time
from pathlib import Path

st.set_page_config(
    page_title="HubSpot Certification Training — Métricas Boss",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .block-container { max-width: 1100px; padding-top: 1rem; }
    h1 { font-size: 2.2rem !important; }
    h2 { font-size: 1.6rem !important; }
    h3 { font-size: 1.3rem !important; }
    .concept-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%);
        border-left: 5px solid #ff7a59;
        padding: 1.2rem;
        border-radius: 0 8px 8px 0;
        margin: 0.8rem 0;
    }
    .big-number {
        font-size: 3rem;
        font-weight: bold;
        color: #ff7a59;
        text-align: center;
    }
    .stButton > button[kind="primary"] {
        background-color: #ff7a59;
        font-size: 1.1rem;
        padding: 0.6rem 2rem;
    }
    div[data-testid="stExpander"] { border: 1px solid #e0e0e0; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)


def load_questions(cert: str) -> list[dict]:
    path = Path(__file__).parent / "questions" / f"{cert}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


CERT1 = load_questions("cert1_implementation")
CERT2 = load_questions("cert2_crm_migration")

# --- SLIDE DEFINITIONS ---
# Each slide is a dict with: title, type (cover/theory/exercise/review/closing), content function

def slide_cover():
    st.markdown("")
    st.markdown("")
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("# HubSpot Certification Training")
        st.markdown("### Métricas Boss — Treinamento Interno")
        st.markdown("---")
        st.markdown("""
        **Certificações cobertas:**
        1. HubSpot Implementation for Partners
        2. CRM Data Migration

        **Duração:** ~1 hora

        **Estrutura:**
        - Revisão de conceitos-chave por módulo
        - Exercícios práticos com questões reais da prova
        - Discussão em grupo + explicações detalhadas
        """)
        st.markdown("---")
        st.markdown("*Pressione* **Próximo** *na barra lateral para começar*")


def slide_agenda():
    st.markdown("## Agenda da Sessão")
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Parte 1 — CRM Data Migration (25 min)

        | Bloco | Tempo | Conteúdo |
        |---|---|---|
        | 1.1 | 5 min | Change Management & ADKAR |
        | 1.2 | 5 min | Processo de Migração |
        | 1.3 | 5 min | Data Modeling & Mapping |
        | 1.4 | 5 min | Testing & Go-Live |
        | 1.5 | 5 min | Exercícios CRM Migration |
        """)

    with col2:
        st.markdown("""
        ### Parte 2 — Implementation (25 min)

        | Bloco | Tempo | Conteúdo |
        |---|---|---|
        | 2.1 | 5 min | Processo & Framework |
        | 2.2 | 5 min | Marketing & Sales Hub |
        | 2.3 | 5 min | Service & Content Hub |
        | 2.4 | 5 min | Reporting & Training |
        | 2.5 | 5 min | Exercícios Implementation |
        """)

    st.markdown("""
    ### Parte 3 — Revisão Final (10 min)
    - Simulado rápido com 10 questões mistas
    - Revisão dos conceitos mais cobrados
    - Dúvidas
    """)


# ========== PART 1: CRM DATA MIGRATION ==========

def slide_p1_title():
    st.markdown("# Parte 1: CRM Data Migration")
    st.markdown("### Certificação: CRM Data Migration")
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="big-number">37</div>', unsafe_allow_html=True)
        st.caption("Questões no banco")
    with col2:
        st.markdown('<div class="big-number">60</div>', unsafe_allow_html=True)
        st.caption("Questões na prova real")
    with col3:
        st.markdown('<div class="big-number">75%</div>', unsafe_allow_html=True)
        st.caption("Nota mínima")
    with col4:
        st.markdown('<div class="big-number">3h</div>', unsafe_allow_html=True)
        st.caption("Tempo na prova real")


def slide_change_mgmt():
    st.markdown("## 1.1 Change Management")
    st.markdown("---")

    st.markdown('<div class="concept-card">', unsafe_allow_html=True)
    st.markdown("""
    **Definição:** Change management é uma abordagem sistemática para alcançar resultados de negócio
    através da execução de mudança. Estado atual → Transição → Estado desejado.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Os 4 Tipos de Mudança")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        | Tipo | Comportamento | Emoção |
        |---|---|---|
        | **Informational** | Sem mudança | Pouca emoção |
        | **Transitional** | Sem mudança | **Resposta emocional** |
        | **Behavioral** | **Mudança significativa** | Pouca emoção |
        | **Transformational** | **Mudança significativa** | **Emoção forte** |
        """)

    with col2:
        st.markdown("""
        ### Modelos

        **ADKAR** (foco em pessoas):
        - **A**wareness — entender POR QUE mudar
        - **D**esire — motivação para participar
        - **K**nowledge — saber COMO mudar (informação)
        - **A**bility — CONSEGUIR fazer (competência)
        - **R**einforcement — manter comportamentos novos

        **Kotter** (8 estágios organizacionais):
        Urgência → Coalizão → Visão → Comunicar → Remover obstáculos → Quick wins → Construir → Ancorar
        """)

    st.markdown("""
    > **Dica de prova:** A diferença entre Knowledge e Ability é a mais cobrada.
    Knowledge = informação teórica. Ability = capacidade prática + confiança.
    """)


def slide_migration_process():
    st.markdown("## 1.2 Processo de Migração")
    st.markdown("---")

    st.markdown('<div class="concept-card">', unsafe_allow_html=True)
    st.markdown("""
    **CRM Data Migration** = processo de mover dados de um CRM para outro (NÃO assets, NÃO CMS).
    É uma oportunidade de **OTIMIZAR**, não replicar processos ruins.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    ### Processo Completo (10 passos)
    ```
    Discovery → Audit → Data Model → Mapping → HubSpot Prep → Cleanup → Test → UAT → Migration → Training
    ```
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Conceitos-Chave

        | Conceito | Definição |
        |---|---|
        | **Cutoff date** | Quando o CRM antigo para de receber dados |
        | **Delta migration** | Migra só o que mudou desde a migração inicial |
        | **Rollback** | Reverter para estado anterior (HubSpot NÃO tem nativo!) |
        | **Ordem de import** | Users → Companies → Contacts → Deals |
        | **Test migration** | ~10% dos records, dados REAIS (não dummy) |
        """)

    with col2:
        st.markdown("""
        ### 3 Métodos de Migração

        1. **APIs** — programático, complexo, precisa dev
        2. **Native import tool** — CSV/spreadsheet, mais simples
        3. **Third-party tools** — ferramentas intermediárias

        ### Big Bang vs Trickle

        | Big Bang | Trickle |
        |---|---|
        | Tudo de uma vez | Em fases |
        | Rápido, mais risco | Mais seguro, mais tempo |
        | Deadlines apertados | Menos risco operacional |
        """)

    st.markdown("""
    ### Antes de Importar — DESLIGAR:
    - Automated contact creation / association com companies
    - Automated property filling (HubSpot Insights)
    - Active integrations e data syncs
    - Workflows e automações ativas
    """)


def slide_data_modeling():
    st.markdown("## 1.3 Data Modeling & Mapping")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Data Modeling

        - **ERDs** (Entity Relationship Diagrams) = flowchart que mostra relações entre objetos
        - Associações no HubSpot são **bidirecionais**
        - **Association labels** definem o tipo de relação (ex: "Decision Maker", "Billing Contact")
        - **Data Model Overview** no HubSpot mostra relações entre objects, properties e activities

        ### Objetos Padrão
        Contacts, Companies, Deals, Tickets, Activities, Custom Objects

        ### Tipos de Property
        - **Enumeration:** Multi-select, Radio select, Checkbox
        - **NÃO enumeration:** Number (campo livre numérico)
        """)

    with col2:
        st.markdown("""
        ### Data Mapping

        **Spreadsheet com tabs por objeto:**
        - Source CRM properties + field values
        - HubSpot properties + field values
        - Field types para todas as properties
        - Transformações necessárias
        - ❌ NÃO inclui workflow actions

        ### Unique Identifiers
        | Objeto | Identificador |
        |---|---|
        | Contacts | Email |
        | Companies | Domain |
        | Deals/Tickets | Record ID |

        ### Import de Contacts — Obrigatório:
        - Email (required unique identifier)
        - First name, Last name (standard)
        - ❌ Job title NÃO é obrigatório
        """)


def slide_testing():
    st.markdown("## 1.4 Testing, UAT & Training")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Test Migration
        - **~10% dos records** como amostra
        - Usar dados **REAIS** (não dummy)
        - Incluir edge cases + records de alto valor
        - Testar ANTES, DURANTE e DEPOIS

        ### Sandbox vs Production
        | Sandbox | Production |
        |---|---|
        | Seguro, controlado | Preciso, mas arriscado |
        | Pode não replicar 100% | Rodar off-hours |
        | Ideal para testes | Desabilitar automações |

        ### Troubleshooting de Import
        - Date parsing failures
        - Missing association records
        - Invalid enumeration options
        - Property validation errors
        - Mapping Preview checa primeiras 100 rows
        """)

    with col2:
        st.markdown("""
        ### UAT (User Acceptance Testing)
        - Testers = **end users reais** (não remover o cliente!)
        - Diversidade de roles e seniority
        - Tarefas claras + guidelines de feedback
        - Fatores: company size, roles, learning preferences, culture

        ### Data Quality Command Center (Operations Hub)
        - Fill rate (%) = % de records com valor para uma property
        - Formatting issues
        - Duplicate records
        - ❌ NÃO identifica unused playbooks

        ### Training & Enablement
        - **Learning objectives** = o que participantes devem saber/fazer APÓS
        - Múltiplos formatos (live, gravado, guias)
        - Treinar por role
        - Managers reforçam em 1:1s com direct reports
        - Adultos são autônomos → dar responsabilidade
        """)


def slide_exercise_crm(questions, start_idx, count, label):
    st.markdown(f"## Exercícios — {label}")
    st.markdown("*Vamos discutir cada questão em grupo. Qual a resposta de vocês?*")
    st.markdown("---")

    subset = questions[start_idx:start_idx + count]

    for i, q in enumerate(subset):
        with st.expander(f"Questão {i+1}: {q['question'][:100]}{'...' if len(q['question']) > 100 else ''}", expanded=False):
            is_multi = q["type"] == "multi"
            if is_multi:
                st.caption("(Múltipla escolha — mais de uma correta)")

            for j, opt in enumerate(q["options"]):
                letter = chr(65 + j)
                st.markdown(f"**{letter}.** {opt}")

            st.markdown("---")

            if st.button(f"Revelar Resposta", key=f"reveal_{label}_{i}"):
                correct = q["correct"]
                opts = q["options"]
                if is_multi:
                    if isinstance(correct, list) and all(len(c) == 1 and c.isalpha() for c in correct):
                        answers = [f"{c}. {opts[ord(c) - 65]}" for c in correct]
                    else:
                        answers = correct if isinstance(correct, list) else [correct]
                    st.success(f"**Resposta:** {', '.join(answers)}")
                else:
                    if isinstance(correct, str) and len(correct) == 1 and correct.isalpha():
                        answer = f"{correct}. {opts[ord(correct) - 65]}"
                    else:
                        answer = correct
                    st.success(f"**Resposta:** {answer}")
                st.info(f"**Explicação:** {q['explanation']}")


def slide_ex_crm_1():
    slide_exercise_crm(CERT2, 0, 6, "CRM Migration — Change Management")

def slide_ex_crm_2():
    slide_exercise_crm(CERT2, 6, 6, "CRM Migration — Processo & Data Quality")

def slide_ex_crm_3():
    slide_exercise_crm(CERT2, 12, 6, "CRM Migration — Modeling, Mapping & Testing")


# ========== PART 2: IMPLEMENTATION ==========

def slide_p2_title():
    st.markdown("# Parte 2: Implementation for Partners")
    st.markdown("### Certificação: HubSpot Implementation for Partners")
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="big-number">61</div>', unsafe_allow_html=True)
        st.caption("Questões no banco")
    with col2:
        st.markdown('<div class="big-number">60</div>', unsafe_allow_html=True)
        st.caption("Questões na prova real")
    with col3:
        st.markdown('<div class="big-number">75%</div>', unsafe_allow_html=True)
        st.caption("Nota mínima")
    with col4:
        st.markdown('<div class="big-number">3h</div>', unsafe_allow_html=True)
        st.caption("Tempo na prova real")


def slide_impl_framework():
    st.markdown("## 2.1 Framework de Implementação")
    st.markdown("---")

    st.markdown('<div class="concept-card">', unsafe_allow_html=True)
    st.markdown("""
    **Regra de ouro:** Goals → Data → Processes → Tools (SEMPRE nessa ordem!)
    A estratégia é guiada pelos objetivos do cliente, não pelas features do HubSpot.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Onboarding vs Implementation

        | | Onboarding | Implementation |
        |---|---|---|
        | Modelo | "Do it with me" | "Do it for me" |
        | Profundidade | Básico | Consultivo, técnico |
        | Escopo | Configuração padrão | Customização completa |

        ### 5 Passos
        ```
        Discovery → Account Setup → Data Migration → Configuration → Enablement
        ```

        ### RACI na Implementação
        - **Partner** = Responsible + Accountable
        - **Cliente** = Consulted + Informed
        - ⚠️ Na prova: partner é R e A, NÃO o cliente!
        """)

    with col2:
        st.markdown("""
        ### 3 Ações por Hub
        | Ação | O que é |
        |---|---|
        | **Migration** | Dados one-time (contacts, deals) |
        | **Integration** | Fluxo contínuo (app conectado) |
        | **Re-creation** | Rebuild no HubSpot (landing pages, forms, templates) |

        ### Equipe (6 funções)
        1. Project Management
        2. Client Strategy
        3. Solutions Architecture
        4. Platform Configuration
        5. Development
        6. Data Migration

        ### Conceitos de Discovery
        - **SMART goals** (Specific, Measurable, Attainable, Relevant, Time-bound)
        - **Reverse demo** = cliente mostra o sistema atual
        - **Migração ANTES de configuração**
        """)


def slide_marketing_sales():
    st.markdown("## 2.2 Marketing Hub & Sales Hub")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Marketing Hub

        | Ferramenta | Uso |
        |---|---|
        | **Campaigns** | Centralizar multi-channel numa interface |
        | **Persona property** | Usado em Lists, Reports, Forms, Ads |
        | **Breeze social agent** | AI para criar posts LinkedIn/Facebook |
        | **Contact scoring** | Lead scoring customizado |
        | **Form automation** | Criar contacts, assign status, trigger workflows |
        | **CTAs** | Suportam vídeo |
        | **Google Search Console** | Avg position, queries, traffic, CTR |

        ### Surveys (DECORAR!)
        | Survey | O que mede |
        |---|---|
        | **NPS** | Likelihood to **refer/recommend** |
        | **CSAT** | Satisfaction com **purchase/feature** |
        | **CES** | Effort em **support interaction** |
        """)

    with col2:
        st.markdown("""
        ### Sales Hub

        | Ferramenta | Uso |
        |---|---|
        | **Deal intelligence** | AI summaries de engagements |
        | **Forecast intelligence** | Projetar vendas futuras |
        | **Pipelines** | Múltiplas pipelines, deal stages, win probability |
        | **Playbooks** | Padronizar best practices do time |
        | **Quote templates** | ❌ NÃO migram, precisam ser RE-CRIADOS |
        | **Workflows** | Podem enviar notificações pro Salesforce |

        ### AI no Sales Hub
        - Outreach personalization
        - Deal prioritization
        - Company record enrichment
        - ❌ Pipeline creation NÃO é AI

        ### Reporting no Sales Hub
        Disponível em: Insights, Sales Content Analytics, Dashboards, Sales Workspace
        """)


def slide_service_content():
    st.markdown("## 2.3 Service Hub & Content Hub")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Service Hub

        | Conceito | Detalhe |
        |---|---|
        | **Conversations inbox** | Visão unificada do cliente |
        | **Múltiplas pipelines** | Sim, suporta |
        | **Knowledge base** | Suporta vídeo |
        | **Setup obrigatório** | Seats + Permissions + Users (NÃO Jobs) |
        | **SLAs** | Setup de Service Hub, NÃO account setup |
        | **Feedback surveys** | Coletar info + personalizar follow-up |
        | **Customer health scores** | Medir product adoption |
        | **AI agents** | Self-service automatizado |

        ### Engagements (atividades)
        - Emails, Meetings, Calls, Tasks, Notes
        - ❌ Associations NÃO são engagements
        """)

    with col2:
        st.markdown("""
        ### Content Hub

        | Ferramenta | O que faz |
        |---|---|
        | **Content embed** | Criar conteúdo HubSpot e embutir em site externo |
        | **Content staging** | Preview/collab antes de publicar |
        | **Content Remix** | Repurpose 1 peça → múltiplos canais |
        | **Smart content** | Personalização dinâmica por segmento |
        | **Memberships** | Gated content / acesso restrito |
        | **Files tool** | Upload de PDFs, imagens, ebooks |
        | **Projects tool** | Organizar tasks de content marketing |
        | **Topics** | Temas-chave para SEO / topic clusters |
        | **Brand Voice** | Consistência de tom AI |

        ### O que NÃO faz
        - ❌ Monetizar conteúdo
        - ❌ A/B testing (isso é Adaptive Testing, não Content Staging)
        - ❌ Não precisa de devs para criar site

        ### WordPress Plugin
        ✅ Forms, popups, live chat, tracking, analytics
        ❌ NÃO inclui content staging
        """)


def slide_reporting_training():
    st.markdown("## 2.4 Reporting, Account Setup & Misc")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Reporting

        | Report | Quando usar |
        |---|---|
        | **Contact attribution** | Qual conteúdo gera mais contatos |
        | **Campaign Analytics** | Comparar performance entre campaigns |
        | **Email scheduling** | Envio automático de dashboards |
        | **Calculated properties** | Podem aparecer em records E reports |
        | **Dados externos** | Sim, é possível reportar sobre eles |

        ### Account Setup Padrão
        ✅ Users, teams, seats, permissions
        ✅ Email e web domains
        ✅ Conectar external tools (apps)
        ❌ SLAs e channels de Help Desk (isso é config do Service Hub)

        ### User Permissions
        Customizáveis: property settings, workflows, bulk actions (tudo)
        """)

    with col2:
        st.markdown("""
        ### Assets que precisam ser RE-CRIADOS
        ✅ Landing pages, Forms, Quote templates, Email templates
        ❌ Images (migram via Files tool)
        ❌ Associations (são dados, não assets)

        ### True/False mais cobrados
        | Afirmação | Resposta |
        |---|---|
        | Mover tudo de uma vez | **False** |
        | Test batch antes | **True** |
        | Website pages via API | **False** |
        | Múltiplas pipelines Service Hub | **True** |
        | Quote templates migram | **False** |
        | Vídeo em CTAs | **True** |
        | Vídeo em knowledge base | **True** |
        | Site sem devs | **True** (False que precisa) |
        | SMS em todos os planos | **False** |
        | Calculated properties em reports | **True** |
        | Report dados externos | **True** |
        | Workflows + Salesforce | **True** (False que não pode) |
        """)


def slide_ex_impl_1():
    slide_exercise_crm(CERT1, 0, 6, "Implementation — Processo & Framework")

def slide_ex_impl_2():
    slide_exercise_crm(CERT1, 6, 6, "Implementation — Hubs & Features")

def slide_ex_impl_3():
    slide_exercise_crm(CERT1, 12, 6, "Implementation — Reporting & Setup")


# ========== PART 3: FINAL REVIEW ==========

def slide_final_quiz():
    st.markdown("## Simulado Final — 10 Questões Mistas")
    st.markdown("*Última rodada! Questões de ambas as certificações.*")
    st.markdown("---")

    mixed = [
        CERT2[0], CERT2[2], CERT2[20], CERT2[28], CERT2[24],
        CERT1[32], CERT1[57], CERT1[14], CERT1[47], CERT1[21],
    ]

    for i, q in enumerate(mixed):
        with st.expander(f"Questão {i+1}: {q['question'][:100]}{'...' if len(q['question']) > 100 else ''}", expanded=False):
            is_multi = q["type"] == "multi"
            if is_multi:
                st.caption("(Múltipla escolha)")

            for j, opt in enumerate(q["options"]):
                letter = chr(65 + j)
                st.markdown(f"**{letter}.** {opt}")

            st.markdown("---")
            if st.button(f"Revelar Resposta", key=f"reveal_final_{i}"):
                correct = q["correct"]
                opts = q["options"]
                if is_multi:
                    if isinstance(correct, list) and all(len(c) == 1 and c.isalpha() for c in correct):
                        answers = [f"{c}. {opts[ord(c) - 65]}" for c in correct]
                    else:
                        answers = correct if isinstance(correct, list) else [correct]
                    st.success(f"**Resposta:** {', '.join(answers)}")
                else:
                    if isinstance(correct, str) and len(correct) == 1 and correct.isalpha():
                        answer = f"{correct}. {opts[ord(correct) - 65]}"
                    else:
                        answer = correct
                    st.success(f"**Resposta:** {answer}")
                st.info(f"**Explicação:** {q['explanation']}")


def slide_cheat_sheet():
    st.markdown("## Resumão — Conceitos Mais Cobrados")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### CRM Data Migration

        1. **4 tipos de mudança** — Informational, Transitional, Behavioral, Transformational
        2. **ADKAR** — Knowledge (info) vs Ability (competência)
        3. **Processo:** Discovery → ... → Training (10 passos)
        4. **Cutoff date** / **Delta migration**
        5. **Ordem import:** Users → Companies → Contacts → Deals
        6. **10% sample** com dados REAIS
        7. **HubSpot NÃO tem rollback** nativo
        8. **Data Quality Command Center** = Operations Hub
        9. **Fill rate** = % de records com valor
        10. **ERD** = flowchart de relações
        11. **Association labels** = definir tipo de relação
        12. **Desabilitar automações** antes de importar
        13. **Custom property** para segmentar dados novos vs existentes
        14. **API NÃO é low-resource** (precisa de devs)
        15. **Project Manager** = comunicação e milestones
        """)

    with col2:
        st.markdown("""
        ### Implementation for Partners

        1. **Goals → Data → Processes → Tools** (ordem!)
        2. **Onboarding** (with me) vs **Implementation** (for me)
        3. **Partner = R + A** no RACI (não o cliente!)
        4. **Migration / Integration / Re-creation** (3 ações)
        5. **Migração ANTES de configuração**
        6. **Surveys:** NPS (referral), CSAT (satisfaction), CES (effort)
        7. **Campaigns** = multi-channel centralizado
        8. **Content Remix** = repurpose com pouco recurso
        9. **Content embed** = conteúdo em site externo
        10. **Content staging ≠ A/B testing**
        11. **Contact attribution** = qual conteúdo gera leads
        12. **Forecast intelligence** = projetar vendas
        13. **Deal intelligence** = AI summaries
        14. **Quote templates NÃO migram**
        15. **Website pages NÃO migram via API**
        """)


def slide_closing():
    st.markdown("")
    st.markdown("")
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("# Parabéns! Treinamento Concluído")
        st.markdown("---")
        st.markdown("""
        ### Próximos Passos

        1. **Fazer a prova** — HubSpot Academy (3h, 60 questões, 75% mínimo)
        2. **Revisar** — Volte nos slides de teoria e no resumão
        3. **Praticar** — Use o modo Quiz Individual (sidebar)
        4. **Dúvidas** — Pergunte no canal do time

        ---

        **Boa sorte na certificação!**

        *Treinamento preparado por Métricas Boss*
        """)


# ========== SLIDE MAP ==========

SLIDES = [
    {"title": "Capa", "fn": slide_cover, "section": "Início"},
    {"title": "Agenda", "fn": slide_agenda, "section": "Início"},
    # Part 1
    {"title": "CRM Migration — Intro", "fn": slide_p1_title, "section": "Parte 1: CRM Migration"},
    {"title": "1.1 Change Management", "fn": slide_change_mgmt, "section": "Parte 1: CRM Migration"},
    {"title": "1.2 Processo de Migração", "fn": slide_migration_process, "section": "Parte 1: CRM Migration"},
    {"title": "1.3 Data Modeling & Mapping", "fn": slide_data_modeling, "section": "Parte 1: CRM Migration"},
    {"title": "1.4 Testing & Training", "fn": slide_testing, "section": "Parte 1: CRM Migration"},
    {"title": "Exercícios — Change Management", "fn": slide_ex_crm_1, "section": "Parte 1: CRM Migration"},
    {"title": "Exercícios — Processo & Data Quality", "fn": slide_ex_crm_2, "section": "Parte 1: CRM Migration"},
    {"title": "Exercícios — Modeling & Testing", "fn": slide_ex_crm_3, "section": "Parte 1: CRM Migration"},
    # Part 2
    {"title": "Implementation — Intro", "fn": slide_p2_title, "section": "Parte 2: Implementation"},
    {"title": "2.1 Framework de Implementação", "fn": slide_impl_framework, "section": "Parte 2: Implementation"},
    {"title": "2.2 Marketing & Sales Hub", "fn": slide_marketing_sales, "section": "Parte 2: Implementation"},
    {"title": "2.3 Service & Content Hub", "fn": slide_service_content, "section": "Parte 2: Implementation"},
    {"title": "2.4 Reporting & Setup", "fn": slide_reporting_training, "section": "Parte 2: Implementation"},
    {"title": "Exercícios — Processo & Framework", "fn": slide_ex_impl_1, "section": "Parte 2: Implementation"},
    {"title": "Exercícios — Hubs & Features", "fn": slide_ex_impl_2, "section": "Parte 2: Implementation"},
    {"title": "Exercícios — Reporting & Setup", "fn": slide_ex_impl_3, "section": "Parte 2: Implementation"},
    # Part 3
    {"title": "Simulado Final", "fn": slide_final_quiz, "section": "Parte 3: Revisão Final"},
    {"title": "Resumão — Cheat Sheet", "fn": slide_cheat_sheet, "section": "Parte 3: Revisão Final"},
    {"title": "Encerramento", "fn": slide_closing, "section": "Parte 3: Revisão Final"},
]


def main():
    if "slide_idx" not in st.session_state:
        st.session_state.slide_idx = 0
    if "training_start" not in st.session_state:
        st.session_state.training_start = None

    with st.sidebar:
        st.markdown("### Navegação")

        if st.session_state.training_start:
            elapsed = time.time() - st.session_state.training_start
            remaining = max(0, 3600 - elapsed)
            m, s = divmod(int(remaining), 60)
            st.metric("Tempo", f"{m:02d}:{s:02d}")
        else:
            if st.button("Iniciar Timer (1h)"):
                st.session_state.training_start = time.time()
                st.rerun()

        st.markdown("---")

        current_section = ""
        for i, slide in enumerate(SLIDES):
            if slide["section"] != current_section:
                current_section = slide["section"]
                st.markdown(f"**{current_section}**")

            is_current = i == st.session_state.slide_idx
            label = f"{'→ ' if is_current else '   '}{slide['title']}"
            if st.button(label, key=f"nav_{i}", use_container_width=True):
                st.session_state.slide_idx = i
                st.rerun()

    # Top navigation bar
    idx = st.session_state.slide_idx
    total_slides = len(SLIDES)

    col1, col2, col3, col4 = st.columns([1, 1, 4, 1])
    with col1:
        if idx > 0:
            if st.button("← Anterior"):
                st.session_state.slide_idx = idx - 1
                st.rerun()
    with col2:
        if idx < total_slides - 1:
            if st.button("Próximo →", type="primary"):
                st.session_state.slide_idx = idx + 1
                st.rerun()
    with col3:
        st.caption(f"Slide {idx + 1}/{total_slides} — {SLIDES[idx]['section']}")
    with col4:
        st.progress((idx + 1) / total_slides)

    st.markdown("---")

    # Render current slide
    SLIDES[idx]["fn"]()


if __name__ == "__main__":
    main()
