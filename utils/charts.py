import plotly.express as px
import plotly.graph_objects as go


def histogram(df, column):
    """Histogram for numeric columns."""
    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"Distribution of {column}"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def box_plot(df, column):
    """Box plot."""
    fig = px.box(
        df,
        y=column,
        title=f"Box Plot - {column}"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def scatter_plot(df, x_col, y_col):
    """Scatter plot."""
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{x_col} vs {y_col}"
    )

    fig.update_layout(
        template="plotly_white",
        height=550
    )

    return fig


def line_chart(df, x, y):
    """Interactive line chart."""

    fig = px.line(
        df,
        x=x,
        y=y,
        title=f"{y} vs {x}",
        markers=True,
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        title_x=0.5,
    )

    return fig


def bar_chart(df, column):
    """Bar chart for categorical columns."""
    counts = (
        df[column]
        .value_counts()
        .reset_index()
    )

    counts.columns = [column, "Count"]

    fig = px.bar(
        counts,
        x=column,
        y="Count",
        title=f"{column} Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def pie_chart(df, column):
    """Pie chart."""
    counts = (
        df[column]
        .value_counts()
        .reset_index()
    )

    counts.columns = [column, "Count"]

    fig = px.pie(
        counts,
        names=column,
        values="Count",
        hole=0.35,
        title=f"{column} Distribution"
    )

    fig.update_layout(
        height=500
    )

    return fig


def correlation_heatmap(df):
    """Correlation heatmap."""

    corr = df.corr(numeric_only=True)

    fig = go.Figure(
        data=go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.columns,
            text=corr.round(2).values,
            texttemplate="%{text}",
            colorscale="RdBu",
            zmid=0
        )
    )

    fig.update_layout(
        title="Correlation Heatmap",
        height=650
    )

    return fig


def value_counts_chart(df, column):
    """Horizontal value-count chart."""

    counts = (
        df[column]
        .value_counts()
        .reset_index()
    )

    counts.columns = [column, "Count"]

    fig = px.bar(
        counts,
        y=column,
        x="Count",
        orientation="h",
        title=f"{column} Frequency"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig