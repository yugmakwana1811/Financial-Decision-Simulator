from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def comparison_frame(results):
    return pd.DataFrame([r.row() for r in results])


def scenario_cost_chart(df):
    return px.bar(df, x="name", y="total_cost", color="name", title="Total monetary cost by scenario", labels={"name": "Scenario", "total_cost": "Rupees"})


def coverage_chart(df):
    shown = df.copy(); shown["coverage_display"] = shown["emergency_coverage"].fillna(0)
    return px.bar(shown, x="name", y="coverage_display", color="name", title="Emergency-fund coverage after decision", labels={"coverage_display": "Months"})


def cashflow_chart(df):
    return px.bar(df, x="name", y="monthly_surplus", color="name", title="Monthly surplus or deficit after decision", labels={"monthly_surplus": "Rupees per month"})


def emi_breakdown(result):
    return go.Figure(data=[go.Bar(name="Principal", x=[result.name], y=[result.total_cost-result.interest_paid]), go.Bar(name="Interest", x=[result.name], y=[result.interest_paid])], layout={"title": "EMI repayment breakdown", "barmode": "stack"})


def savings_timeline(profile, results, months=24):
    rows=[]
    for r in results:
        for month in range(months+1):
            monthly_change = r.monthly_surplus
            value = r.savings_remaining + month * monthly_change
            rows.append({"Month": month, "Savings": value, "Scenario": r.name})
    return px.line(pd.DataFrame(rows), x="Month", y="Savings", color="Scenario", title="Illustrative savings path under constant-input assumption")
