import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    import plotly.express as px
    import plotly.graph_objects as go

    return go, px


@app.cell
def _(pd):
    file_path = 'DataScientist_CaseStudy_Dataset.xlsx'
    excel_data = pd.ExcelFile(file_path)
    return excel_data, file_path


@app.cell
def _(excel_data):
    description_df = excel_data.parse('Description')
    soc_dem_df = excel_data.parse('Soc_Dem')
    products_df = excel_data.parse('Products_ActBalance')
    inflow_outflow_df = excel_data.parse('Inflow_Outflow')
    sales_revenues_df = excel_data.parse('Sales_Revenues')
    return (
        description_df,
        inflow_outflow_df,
        products_df,
        sales_revenues_df,
        soc_dem_df,
    )


@app.cell
def _(soc_dem_df):
    soc_dem_df
    return


@app.cell
def _(products_df):
    products_df
    return


@app.cell
def _(inflow_outflow_df):
    inflow_outflow_df
    return


@app.cell
def _(sales_revenues_df):
    sales_revenues_df
    return


@app.cell
def _(inflow_outflow_df, products_df, sales_revenues_df, soc_dem_df):
    # Merge datasets on 'Client'
    merged_df = soc_dem_df
    merged_df = merged_df.merge(products_df, on='Client', how='left')
    merged_df = merged_df.merge(inflow_outflow_df, on='Client', how='left')
    merged_df = merged_df.merge(sales_revenues_df, on='Client', how='left')
    return (merged_df,)


@app.cell
def _(merged_df):
    print("Dataset Shape:", merged_df.shape)
    print("\nColumns:", merged_df.columns.tolist())
    print("\nMissing Values:\n", merged_df.isnull().sum())

    return


@app.cell
def _(merged_df):
    # Summary statistics
    print("\nSummary Statistics:\n", merged_df.describe())

    return


@app.cell
def _(px, soc_dem_df):
    # Exploratory Visualizations
    fig1 = px.scatter_matrix(soc_dem_df, dimensions=['Age', 'Tenure'], color='Sex', title="Social-Demographic Data Distribution")
    fig1.show()

    return (fig1,)


@app.cell
def _(go, merged_df):
    # Correlation Heatmap
    correlation_matrix = merged_df.corr()
    fig2 = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.index,
        colorscale='Viridis'))
    fig2.update_layout(title="Correlation Heatmap")
    fig2.show()


    return correlation_matrix, fig2


@app.cell
def _(go, merged_df):

    # Distribution of Product Sales
    sales_columns = ['Sale_MF', 'Sale_CC', 'Sale_CL']
    sales_sum = merged_df[sales_columns].sum()
    fig3 = go.Figure([go.Bar(x=sales_columns, y=sales_sum, text=sales_sum, textposition='auto')])
    fig3.update_layout(title="Product Sales Distribution", xaxis_title="Products", yaxis_title="Count")
    fig3.show()


    return fig3, sales_columns, sales_sum


@app.cell
def _(go, merged_df):
    # Check Revenue Distribution
    revenue_columns = ['Revenue_MF', 'Revenue_CC', 'Revenue_CL']
    revenue_sum = merged_df[revenue_columns].sum()
    fig4 = go.Figure([go.Bar(x=revenue_columns, y=revenue_sum, text=revenue_sum, textposition='auto')])
    fig4.update_layout(title="Revenue Distribution by Product", xaxis_title="Products", yaxis_title="Total Revenue")
    fig4.show()


    return fig4, revenue_columns, revenue_sum


@app.cell
def _(merged_df):
    # Export merged dataset for Marimo
    output_file_path = 'merged_dataset.csv'
    merged_df.to_csv(output_file_path, index=False)
    print(f"Merged dataset exported to {output_file_path}")

    return (output_file_path,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
