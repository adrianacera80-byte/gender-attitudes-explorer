import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gender Attitudes Explorer", layout="centered")

@st.cache_data
def load_data():
    return pd.read_pickle("df_gender_clean.pkl")

df_gender = load_data()

var_info = {
    "likrisk_lab": {
        "label": "Likes to take risks",
        "description": "Extent to which the respondent says: I like to take risks."
    },
    "liklead_lab": {
        "label": "Likes to be a leader",
        "description": "Extent to which the respondent says: I like to be a leader."
    },
    "sothnds_lab": {
        "label": "Sensitive to others' needs",
        "description": "Extent to which the respondent says: I am sensitive to others' needs."
    },
    "actcomp_lab": {
        "label": "Acts compassionately",
        "description": "Extent to which the respondent says: I act compassionately towards others."
    },
    "femifel_lab": {
        "label": "Feels feminine",
        "description": "Overall, how feminine the respondent feels."
    },
    "impbemw_lab": {
        "label": "Importance of being a man/woman",
        "description": "How important being a man or a woman is to the way the respondent thinks about themself."
    },
    "trmedmw_lab": {
        "label": "Unfair treatment in medical care",
        "description": "Experienced unfair treatment when visiting a doctor or seeking medical treatment because of being a man/woman."
    },
    "trwrkmw_lab": {
        "label": "Unfair treatment at work",
        "description": "Experienced unfair treatment in hiring, pay or promotion because of being a man/woman."
    },
    "trmdcnt_lab": {
        "label": "Fairness in medical treatment",
        "description": "Perception of whether women and men are treated equally fairly when seeking medical treatment in the country."
    },
    "trwkcnt_lab": {
        "label": "Fairness at work",
        "description": "Perception of whether women and men are treated equally fairly in hiring, pay or promotion at work in the country."
    },
    "trplcnt_lab": {
        "label": "Fairness of police treatment",
        "description": "Perception of whether the police treat women and men equally fairly in the country."
    },
    "eqwrkbg_lab": {
        "label": "Equal paid work and family life",
        "description": "How bad or good it is for family life if equal numbers of women and men are in paid work."
    },
    "eqpolbg_lab": {
        "label": "Equal political leadership",
        "description": "How bad or good it is for politics if equal numbers of women and men are in political leadership positions."
    },
    "eqmgmbg_lab": {
        "label": "Equal higher management",
        "description": "How bad or good it is for businesses if equal numbers of women and men are in higher management positions."
    },
    "eqpaybg_lab": {
        "label": "Equal pay for same work",
        "description": "How bad or good it is for the economy if women and men receive equal pay for doing the same work."
    },
    "freinsw_lab": {
        "label": "Firing insulting employees",
        "description": "Support or opposition to firing employees who make insulting comments directed at women in the workplace."
    },
    "fineqpy_lab": {
        "label": "Fining unequal pay",
        "description": "Support or opposition to making businesses pay a fine when they pay men more than women for the same work."
    },
    "wsekpwr_lab": {
        "label": "Women seek power over men",
        "description": "How often, in the respondent's opinion, women seek to gain power by getting control over men."
    },
    "weasoff_lab": {
        "label": "Women get easily offended",
        "description": "How often, in the respondent's opinion, women get easily offended."
    },
    "wlespdm_lab": {
        "label": "Women paid less than men",
        "description": "How often, in the respondent's opinion, women are paid less than men for the same work in the country."
    },
    "wexashr_lab": {
        "label": "Women exaggerate harassment claims",
        "description": "How often, in the respondent's opinion, women exaggerate claims of sexual harassment in the workplace."
    },
    "wprtbym_lab": {
        "label": "Women should be protected by men",
        "description": "Agreement or disagreement with the statement that women should be protected by men."
    },
    "wbrgwrm_lab": {
        "label": "Women have better moral sense",
        "description": "Agreement or disagreement with the statement that women tend to have a better sense of right and wrong than men."
    }
}

def get_var_title(var_name):
    if var_name in var_info:
        return var_info[var_name]["label"], var_info[var_name]["description"]
    return var_name, ""

def apply_clean_plotly_style(fig, title_label):
    fig.update_layout(
        template="simple_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        title={
            "text": title_label,
            "x": 0.5,
            "xanchor": "center"
        },
        legend_title="Category",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.22,
            xanchor="center",
            x=0.5
        ),
        margin=dict(t=60, r=20, b=110, l=20),
        font=dict(size=11)
    )
    fig.update_xaxes(
        range=[0, 100],
        title="Percent",
        showgrid=False,
        zeroline=False
    )
    fig.update_yaxes(
        showgrid=False,
        zeroline=False,
        title=None,
        automargin=True
    )
    return fig

def filter_data(df, selected_countries):
    df_filtered = df.copy()

    if selected_countries:
        df_filtered = df_filtered[df_filtered["cntry_lab"].isin(selected_countries)]

    return df_filtered

def plot_lab_by_gender(df, var_lab, gender_col="gndr"):
    tab = pd.crosstab(
        df[gender_col],
        df[var_lab],
        normalize="index"
    ).mul(100).reset_index()

    long_df = tab.melt(
        id_vars=gender_col,
        var_name="category",
        value_name="percent"
    )

    title_label, _ = get_var_title(var_lab)

    fig = px.bar(
        long_df,
        y=gender_col,
        x="percent",
        color="category",
        orientation="h",
        barmode="stack",
        labels={gender_col: "Gender", "category": "Category"},
        hover_data={"percent": ":.2f"},
        height=320
    )

    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Category: %{fullData.name}<br>Percent: %{x:.2f}%<extra></extra>"
    )

    return apply_clean_plotly_style(fig, title_label)

def plot_lab_by_country(df, var_lab, country_col="cntry_lab"):
    tab = pd.crosstab(
        df[country_col],
        df[var_lab],
        normalize="index"
    ).mul(100).reset_index()

    long_df = tab.melt(
        id_vars=country_col,
        var_name="category",
        value_name="percent"
    )

    title_label, _ = get_var_title(var_lab)
    n_countries = df[country_col].nunique()

    fig = px.bar(
        long_df,
        y=country_col,
        x="percent",
        color="category",
        orientation="h",
        barmode="stack",
        labels={country_col: "Country", "category": "Category"},
        hover_data={"percent": ":.2f"},
        height=max(420, n_countries * 32)
    )

    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Category: %{fullData.name}<br>Percent: %{x:.2f}%<extra></extra>"
    )

    return apply_clean_plotly_style(fig, title_label)

def plot_lab_by_country_gender(df, var_lab, country_col="cntry_lab", gender_col="gndr"):
    tab = pd.crosstab(
        [df[country_col], df[gender_col]],
        df[var_lab],
        normalize="index"
    ).mul(100).reset_index()

    tab["country_gender"] = (
        tab[country_col].astype(str) + " - " + tab[gender_col].astype(str)
    )

    long_df = tab.melt(
        id_vars=["country_gender"],
        var_name="category",
        value_name="percent"
    )

    title_label, _ = get_var_title(var_lab)
    n_rows = tab["country_gender"].nunique()

    fig = px.bar(
        long_df,
        y="country_gender",
        x="percent",
        color="category",
        orientation="h",
        barmode="stack",
        labels={"country_gender": "Country - Gender", "category": "Category"},
        hover_data={"percent": ":.2f"},
        height=max(500, n_rows * 30)
    )

    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Category: %{fullData.name}<br>Percent: %{x:.2f}%<extra></extra>"
    )

    return apply_clean_plotly_style(fig, title_label)

def plot_lab_by_age_gender(df, var_lab, age_col="agegroup", gender_col="gndr"):
    tab = pd.crosstab(
        [df[age_col], df[gender_col]],
        df[var_lab],
        normalize="index"
    ).mul(100).reset_index()

    tab["age_gender"] = (
        tab[age_col].astype(str) + " - " + tab[gender_col].astype(str)
    )

    long_df = tab.melt(
        id_vars=["age_gender"],
        var_name="category",
        value_name="percent"
    )

    title_label, _ = get_var_title(var_lab)
    n_rows = tab["age_gender"].nunique()

    fig = px.bar(
        long_df,
        y="age_gender",
        x="percent",
        color="category",
        orientation="h",
        barmode="stack",
        labels={"age_gender": "Age group - Gender", "category": "Category"},
        hover_data={"percent": ":.2f"},
        height=max(420, n_rows * 34)
    )

    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Category: %{fullData.name}<br>Percent: %{x:.2f}%<extra></extra>"
    )

    return apply_clean_plotly_style(fig, title_label)

st.title("Gender Attitudes Explorer")
st.caption("Explore gender attitudes across countries, gender groups and age groups.")

lab_vars = sorted(var_info.keys())
nice_options = {var_info.get(col, {"label": col})["label"]: col for col in lab_vars}

countries = sorted(df_gender["cntry_lab"].dropna().unique())

with st.sidebar:
    st.header("Explore")

    selected_label = st.selectbox(
        "Choose a variable",
        list(nice_options.keys())
    )

    plot_type = st.selectbox(
        "Choose a plot",
        ["By gender", "By country", "By country and gender", "By age and gender"]
    )

    selected_countries = st.multiselect(
        "Filter countries",
        countries,
        default=countries[:5] if len(countries) > 5 else countries
    )

selected_var = nice_options[selected_label]
label, description = get_var_title(selected_var)

df_filtered = filter_data(df_gender, selected_countries)

st.subheader(label)
st.caption(description)

col1, col2 = st.columns(2)
col1.metric("Observations", f"{len(df_filtered):,}")
col2.metric("Countries", df_filtered["cntry_lab"].nunique())

if len(df_filtered) == 0:
    st.warning("No data available for the selected filters.")
else:
    if plot_type == "By gender":
        fig = plot_lab_by_gender(df_filtered, selected_var)
    elif plot_type == "By country":
        fig = plot_lab_by_country(df_filtered, selected_var)
    elif plot_type == "By country and gender":
        fig = plot_lab_by_country_gender(df_filtered, selected_var)
    else:
        fig = plot_lab_by_age_gender(df_filtered, selected_var)

    st.plotly_chart(fig, use_container_width=True)
