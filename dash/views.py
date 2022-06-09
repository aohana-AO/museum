from django.shortcuts import render
from django.views.generic import TemplateView  # ❶
import plotly.graph_objects as go


def line_charts():
    fig = go.Figure(
        go.Scatter(x=[1, 2, 3,4,5], y=[3, 5, 2,6,7]), layout=go.Layout(width=700, height=700)
    )
    return fig.to_html(include_plotlyjs=False)  # ❷


class LineChartsView(TemplateView):  # ❶
    template_name = "dash.html"

    def get_context_data(self, **kwargs):
        context = super(LineChartsView, self).get_context_data(**kwargs)
        context["dash"] = line_charts()  # ❸
        return context
