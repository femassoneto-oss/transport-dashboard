# dashboard.py
"""
Streamlit front‑end for the Transport Dashboard.
It uses the pure‑Python `analysis.py` (no pandas / numpy) and Plotly for charts.
"""

import streamlit as st
import plotly.express as px
# pandas removed to avoid numpy dependency

from analysis import get_dashboard_data

st.set_page_config(
    page_title="Transport Executive Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🚚 Transport Executive Dashboard")
st.caption("Generated from `data(51).xlsx` – insights for operations, clients and fleet efficiency")
st.caption("Generated from `data(51).xlsx` – insights for operations, clients and fleet efficiency")

# ---------------------------------------------------------------------------
# Load data (cached so it runs only once per session)
# ---------------------------------------------------------------------------
@st.cache_data(ttl=300)
def load_data():
    return get_dashboard_data()

data = load_data()

# ---------------------------------------------------------------------------
# KPI cards – total plates, total revenue, average productivity
# ---------------------------------------------------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total de placas", value=data["total_plates"])
with col2:
    total_rev = sum(data["revenue_per_operation"].values())
    st.metric(label="Faturamento total (R$)", value=f"{total_rev:,.2f}")
with col3:
    prod_vals = [row.get("productivity", 0) for row in data["raw"]]
    avg_prod = sum(prod_vals) / len(prod_vals) if prod_vals else 0
    st.metric(label="Produtividade média", value=f"{avg_prod:,.2f}")

st.markdown("---")

# ---------------------------------------------------------------------------
# Charts
# ---------------------------------------------------------------------------
# 1. Placas por operação (bar)
plates_op = data["plates_per_operation"]
fig1 = px.bar(
    x=list(plates_op.keys()),
    y=list(plates_op.values()),
    labels={"x": "Operação", "y": "Placas"},
    title="Placas por operação",
    template="plotly_dark",
)
st.plotly_chart(fig1, use_container_width=True)

# 2. Faturamento por operação (pie)
rev_op = data["revenue_per_operation"]
fig2 = px.pie(
    names=list(rev_op.keys()),
    values=list(rev_op.values()),
    title="Faturamento por operação",
    template="plotly_dark",
)
st.plotly_chart(fig2, use_container_width=True)

# 3. Placas exclusivas por cliente (bar – top 10)
client_plates = data["unique_plates_per_client"]
sorted_clients = dict(sorted(client_plates.items(), key=lambda item: item[1], reverse=True)[:10])
fig3 = px.bar(
    x=list(sorted_clients.keys()),
    y=list(sorted_clients.values()),
    labels={"x": "Cliente", "y": "Placas exclusivas"},
    title="Top 10 clientes – placas exclusivas",
    template="plotly_dark",
)
st.plotly_chart(fig3, use_container_width=True)

# 4. Placas que operaram em março e não em abril (list)
if data["march_not_april"]:
    st.subheader("Placas que operaram em março e não em abril")
    st.write(data["march_not_april"])
else:
    st.subheader("Nenhuma placa encontrada que operou em março e não em abril")

# 5. Placas compartilhadas entre operações (grouped bar)
shared = data["shared_plates"]
if shared:
    plate_counts = {}
    for plate, op in shared:
        plate_counts.setdefault(plate, set()).add(op)
    counts = [len(ops) for ops in plate_counts.values()]
    labels = list(plate_counts.keys())
    fig5 = px.bar(
        x=labels,
        y=counts,
        labels={"x": "Placa", "y": "Número de operações"},
        title="Placas compartilhadas (quantas operações)",
        template="plotly_dark",
    )
    st.plotly_chart(fig5, use_container_width=True)
else:
    st.info("Nenhuma placa foi encontrada em mais de uma operação.")

# 6. Ranking das placas (table)
rank_list = data["plate_ranking"][:20]
st.subheader("Ranking das 20 placas com maior faturamento")
st.table(rank_list)

# 7. Operações com maior crescimento (bar) – using pure lists

    growth = data["growth_operations"]
    # sort by growth_pct descending
    growth_sorted = sorted(growth, key=lambda x: x["growth_pct"], reverse=True)
    fig7 = px.bar(
        x=[g["operation"] for g in growth_sorted],
        y=[g["growth_pct"] for g in growth_sorted],
        hover_data={"prev_month": [g["prev_month"] for g in growth_sorted], "cur_month": [g["cur_month"] for g in growth_sorted]},
        title="Operações – maior crescimento percentual (mês a mês)",
        labels={"y": "% de crescimento"},
        template="plotly_dark",
    )
    st.plotly_chart(fig7, use_container_width=True)
else:
    st.info("Não foram detectados crescimentos de receita entre meses.")

# 8. Clientes mais representativos (table)
clients_list = data["top_clients"][:10]
st.subheader("Top 10 clientes – representatividade combinada (receita + placas)")
st.table(clients_list)

# ---------------------------------------------------------------------------
# Automatic insights panel
# ---------------------------------------------------------------------------
st.markdown("---")
st.subheader("💡 Insights automáticos")
for insight in data["insights"]:
    st.write(insight)





st.caption("Generated from `data(51).xlsx` – insights for operations, clients and fleet efficiency")

# ---------------------------------------------------------------------------
# Load data (cached so it runs only once per session
# ---------------------------------------------------------------------------
@st.cache_data(ttl=300)
def load_data():
    return get_dashboard_data()

data = load_data()

# ---------------------------------------------------------------------------
# KPI cards – total plates, total revenue, average productivity
# ---------------------------------------------------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total de placas", value=data["total_plates"])
with col2:
    total_rev = sum(data["revenue_per_operation"].values())
    st.metric(label="Faturamento total (R$)", value=f"{total_rev:,.2f}")
with col3:
    # média de produtividade (somatória / número de registros)
    prod_vals = [row.get("productivity", 0) for row in data["raw"]]
    avg_prod = sum(prod_vals) / len(prod_vals) if prod_vals else 0
    st.metric(label="Produtividade média", value=f"{avg_prod:,.2f}")

st.markdown("---")

# ---------------------------------------------------------------------------
# Charts
# ---------------------------------------------------------------------------
# 1. Placas por operação (bar)
plates_op = data["plates_per_operation"]
fig1 = px.bar(
    x=list(plates_op.keys()),
    y=list(plates_op.values()),
    labels={"x": "Operação", "y": "Placas"},
    title="Placas por operação",
    template="plotly_dark",
)
st.plotly_chart(fig1, use_container_width=True)

# 2. Faturamento por operação (pie)
rev_op = data["revenue_per_operation"]
fig2 = px.pie(
    names=list(rev_op.keys()),
    values=list(rev_op.values()),
    title="Faturamento por operação",
    template="plotly_dark",
)
st.plotly_chart(fig2, use_container_width=True)

# 3. Placas exclusivas por cliente (bar – top 10)
client_plates = data["unique_plates_per_client"]
# order descending and keep top 10
sorted_clients = dict(sorted(client_plates.items(), key=lambda item: item[1], reverse=True)[:10])
fig3 = px.bar(
    x=list(sorted_clients.keys()),
    y=list(sorted_clients.values()),
    labels={"x": "Cliente", "y": "Placas exclusivas"},
    title="Top 10 clientes – placas exclusivas",
    template="plotly_dark",
)
st.plotly_chart(fig3, use_container_width=True)

# 4. Placas que operaram em março e não em abril (list)
if data["march_not_april"]:
    st.subheader("Placas que operaram em março e não em abril")
    st.write(data["march_not_april"])
else:
    st.subheader("Nenhuma placa encontrada que operou em março e não em abril")

# 5. Placas compartilhadas entre operações (network‑style bar)
shared = data["shared_plates"]
if shared:
    # Show shared plates as a simple grouped bar chart
    if shared:
        # Count how many operations each plate appears in
        plate_counts = {}
        for plate, op in shared:
            plate_counts.setdefault(plate, set()).add(op)
        counts = [len(ops) for ops in plate_counts.values()]
        labels = list(plate_counts.keys())
        fig5 = px.bar(
            x=labels,
            y=counts,
            labels={"x": "Placa", "y": "Número de operações"},
            title="Placas compartilhadas (quantas operações)",
            template="plotly_dark",
        )
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.info("Nenhuma placa foi encontrada em mais de uma operação.")
else:
    st.info("Nenhuma placa foi encontrada em mais de uma operação.")

# 6. Ranking das placas (table)
rank_list = data["plate_ranking"][:20]
st.subheader("Ranking das 20 placas com maior faturamento")
st.table(rank_list)

# 7. Operações com maior crescimento (bar)


# 8. Clientes mais representativos (table)
clients_list = data["top_clients"][:10]
st.subheader("Top 10 clientes – representatividade combinada (receita + placas)")
st.table(clients_list)

# ---------------------------------------------------------------------------
# Automatic insights panel
# ---------------------------------------------------------------------------
st.markdown("---")
st.subheader("💡 Insights automáticos")
for insight in data["insights"]:
    st.write(insight)

# Footer
st.caption("Dashboard gerado por Antigravity AI – versão 2026.03")
