# import pandas as pd
# import plotly.express as px

# df = pd.read_csv('data/sample.csv')

# # Geographic Scatter Plot
# fig = px.scatter_geo(df,
#     lat="decimalLatitude",
#     lon="decimalLongitude",
#     hover_name="speciesQueried",
#     color="country",
#     title="Geographical Distribution of Callitrichidae Specimens",
#     projection="natural earth"
# )

# # Density Heatmap
# hotspot_map = px.density_mapbox(
#     df,
#     lat="decimalLatitude",
#     lon="decimalLongitude",
#     radius=8,
#     zoom=3,
#     color_continuous_scale="Viridis",
#     mapbox_style="carto-positron",
#     title="Spatial Density Analysis of Callitrichidae Populations"
# )

# # Species Richness Analysis
# richness = df.groupby("country")["speciesQueried"].nunique().reset_index(name="richness")
# richness_plot = px.bar(
#     richness.sort_values("richness", ascending=False),
#     x="country",
#     y="richness",
#     title="Callitrichidae Species Richness by Geographic Region"
# )

# # Hierarchical Distribution Analysis
# df_treemap = df.groupby(["country", "speciesQueried"]).size().reset_index(name="count")
# treemap_plot = px.treemap(
#     df_treemap,
#     path=["country", "speciesQueried"],
#     values="count",
#     color="count",
#     title="Taxonomic and Geographic Distribution of Callitrichidae Specimens"
# )

# # Life Stage Temporal Analysis
# life_stage_trend = df[df["lifeStage"].notna() & (df["lifeStage"].str.lower() != "unknown")]
# life_stage_plot_data = life_stage_trend.groupby(["year", "lifeStage"]).size().reset_index(name="count")
# life_stage_plot = px.line(
#     life_stage_plot_data,
#     x="year",
#     y="count",
#     color="lifeStage",
#     title="Ontogenetic Distribution of Callitrichidae Observations: Temporal Analysis"
# )

# # Displays
# import preswald

# preswald.text("# Biogeographical Analysis of Callitrichidae Distribution Patterns")

# preswald.text("## Spatial Distribution Analysis")
# preswald.text("Figure 1 illustrates the geographical distribution of Callitrichidae specimens across their native range. Individual data points represent documented occurrences, with color differentiation by country to facilitate identification of biogeographical patterns and potential ecological niches.")
# preswald.plotly(fig)

# preswald.text("## Population Density Assessment")
# preswald.text("Figure 2 presents a kernel density estimation of Callitrichidae observations, highlighting regions of significant population concentration. This visualization aids in identifying critical habitat zones and potential conservation priority areas for these neotropical primates.")
# preswald.plotly(hotspot_map)

# preswald.text("## Species Richness Evaluation")
# preswald.text("Figure 3 quantifies Callitrichidae taxonomic diversity across political boundaries. This analysis reveals significant variation in species richness among countries, potentially reflecting both natural biogeographical patterns and sampling bias considerations.")
# preswald.plotly(richness_plot)

# preswald.text("## Taxonomic Distribution by Geographic Region")
# preswald.text("Figure 4 depicts the hierarchical relationship between geographic distribution and taxonomic classification within the Callitrichidae family. The proportional representation illustrates both abundance and diversity patterns across the study area, with implications for understanding evolutionary and ecological relationships.")
# preswald.plotly(treemap_plot)

# preswald.text("## Ontogenetic Temporal Distribution")
# preswald.text("Figure 5 examines the temporal distribution of Callitrichidae specimens across different life stages. This longitudinal analysis may reveal important demographic shifts, reproductive patterns, or methodological biases in data collection that warrant further investigation.")
# preswald.plotly(life_stage_plot)

from preswald import connect, get_df, table, sidebar, table, text, selectbox, query, image, topbar
import pandas as pd

connect()

sidebar(defaultopen = True)
topbar()
df = get_df('sample_csv')
# print(df.dtypes)
# pd_df = pd.read_csv("data/sample.csv")
# print(pd_df.dtypes)
df['Ash (%)'] = [float(i) for i in df['Ash (%)']]
df['Moisture (%)'] = [float(i) for i in df['Moisture (%)']]
text("***Structured AI Assessment, by Meghshanth Sara***")
text("# Data of Cinnamon Quality Classification.")
text("**About**: This dataset contains 60 balanced synthetic records representing chemical composition of Ceylon cinnamon samples, classified into three quality levels: High, Medium, and Low. Each class contains 20 samples, generated based on research standards and typical value ranges from academic studies. [Link to Dataset](https://www.kaggle.com/datasets/madaraweerasingha/cinnamon-quality-classification).")
image(
    src = "https://images.pexels.com/photos/301669/pexels-photo-301669.jpeg?_gl=1*45w7t*_ga*MTU3OTc5NTA4LjE3NTE0NjMxMjk.*_ga_8JE65Q40S6*czE3NTE0NjMxMjgkbzEkZzEkdDE3NTE0NjMxNDckajQxJGwwJGgw",
    alt= "Cinnamon"
)
text("\n")
table(df)

# sql = "SELECT * FROM sample WHERE Moisture = '10.00'"
# sql = """
#     SELECT * FROM sample_csv
#     WHERE Moisture > 10.00
# """

try:
    filtered_df = query("""SELECT * FROM sample_csv WHERE "Moisture (%)" > 12""", 'sample_csv')
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Query error: {e}")

# filtered_df = query(sql, 'sample_csv')
# print(filtered_df)
# table(filtered_df)



text("# My Data Analysis App")
text("\n")
# table(filtered_df, title="Filtered Data")

choice = selectbox(
    label = "Choose a plot",
    options=["Filtered table","Scatter", "Pie"]
)
from preswald import slider
from preswald import plotly
import plotly.express as px

if choice == "Filtered table":
#    df['Moisture (%)'] = [float(i) for i in df['Moisture (%)']]
    threshold = slider("Threshold", min_val=11, max_val=13, default=12)
    table(df[df["Moisture (%)"] > threshold], title="Dynamic Data View")

elif choice == "Scatter":
    # plot = checkbox(label="Show the plot!")
    fig = px.scatter(df, x="Ash (%)", y="Moisture (%)",color="Quality_Label", hover_name="Sample_ID", title="Scatter Plot Ash v/s Moisture")
    plotly(fig, size= 0.5)

elif choice == "Pie":
    # if plot:
    # pie = checkbox(label="Show me the pie!")
    pie = px.pie(df, names="Quality_Label", title="Percentage of each Quality")
    plotly(pie, 0.5)
    # if pie:  
heat = px.density_heatmap(df, "Ash (%)", "Moisture (%)")
# heat.update_layout(yaxis=dict(autorange = "reversed"))
plotly(heat)