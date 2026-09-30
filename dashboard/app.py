import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CyberShield Analytics",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv("dataset/cyberattacks.csv")


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🛡️ CyberShield")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Overview",
        "📊 Attack Analysis",
        "💰 Impact Analysis",
        "🔐 Security Analysis",
        "🤖 ML Prediction"
    ]
)


# ============================================================
# MAIN TITLE
# ============================================================

st.title("🛡️ CyberShield Analytics")

st.subheader(
    "Analysis and Prediction of Global Cyberattack Trends"
)


# ============================================================
# OVERVIEW PAGE
# ============================================================

if page == "🏠 Overview":

    st.header("📊 Dashboard Overview")

    st.write(
        """
        CyberShield Analytics is a data science and machine learning
        project for analyzing global cyberattack trends from 2015 to 2024.
        The dashboard examines attack patterns, financial impact,
        affected users, vulnerabilities, defense mechanisms and
        machine-learning-based attack prediction.
        """
    )

    # Dashboard metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Incidents",
            len(df)
        )

    with col2:
        st.metric(
            "Countries",
            df["Country"].nunique()
        )

    with col3:
        st.metric(
            "Attack Types",
            df["Attack Type"].nunique()
        )

    with col4:
        st.metric(
            "Target Industries",
            df["Target Industry"].nunique()
        )

    st.divider()

    # Dataset information
    st.subheader("📁 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Data Period:** 2015 – 2024")
        st.write("**Total Records:**", len(df))
        st.write("**Total Features:**", len(df.columns))

    with col2:
        st.write("**Countries:**", df["Country"].nunique())
        st.write("**Attack Types:**", df["Attack Type"].nunique())
        st.write(
            "**Target Industries:**",
            df["Target Industry"].nunique()
        )

    # Dataset preview
    st.subheader("🔍 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )


# ============================================================
# ATTACK ANALYSIS PAGE
# ============================================================

elif page == "📊 Attack Analysis":

    st.header("📊 Cyberattack Analysis")

    st.write(
        """
        This section explores the distribution and trends of
        different cyberattack types, countries and target industries.
        """
    )

    # Attack type distribution
    st.subheader("🎯 Attack Type Distribution")

    attack_counts = df["Attack Type"].value_counts()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.bar_chart(attack_counts)

    with col2:
        st.dataframe(
            attack_counts.rename("Number of Incidents"),
            use_container_width=True
        )

    # Country analysis
    st.subheader("🌍 Cyberattacks by Country")

    country_counts = df["Country"].value_counts()

    st.bar_chart(country_counts)

    # Target industry
    st.subheader("🏢 Cyberattacks by Target Industry")

    industry_counts = df["Target Industry"].value_counts()

    st.bar_chart(industry_counts)

    # Yearly trend
    st.subheader("📈 Cyberattack Trend by Year")

    yearly_attacks = (
        df.groupby("Year")
        .size()
    )

    st.line_chart(yearly_attacks)

    # Attack type vs industry
    st.subheader("🔥 Attack Type vs Target Industry")

    attack_industry = pd.crosstab(
        df["Attack Type"],
        df["Target Industry"]
    )

    st.dataframe(
        attack_industry,
        use_container_width=True
    )


# ============================================================
# IMPACT ANALYSIS PAGE
# ============================================================

elif page == "💰 Impact Analysis":

    st.header("💰 Cyberattack Impact Analysis")

    st.write(
        """
        This section examines financial loss, affected users
        and incident resolution time.
        """
    )

    # Financial loss
    total_loss = (
        df["Financial Loss (in Million $)"].sum()
    )

    average_loss = (
        df["Financial Loss (in Million $)"].mean()
    )

    maximum_loss = (
        df["Financial Loss (in Million $)"].max()
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Financial Loss",
            f"${total_loss:,.2f}M"
        )

    with col2:
        st.metric(
            "Average Loss / Incident",
            f"${average_loss:,.2f}M"
        )

    with col3:
        st.metric(
            "Maximum Loss",
            f"${maximum_loss:,.2f}M"
        )

    st.divider()

    # Financial loss by attack type
    st.subheader(
        "💵 Average Financial Loss by Attack Type"
    )

    loss_by_attack = (
        df.groupby("Attack Type")[
            "Financial Loss (in Million $)"
        ]
        .mean()
        .sort_values(ascending=False)
    )

    st.bar_chart(loss_by_attack)

    # Affected users
    st.subheader("👥 Affected Users")

    total_users = (
        df["Number of Affected Users"].sum()
    )

    average_users = (
        df["Number of Affected Users"].mean()
    )

    maximum_users = (
        df["Number of Affected Users"].max()
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Affected Users",
            f"{total_users:,}"
        )

    with col2:
        st.metric(
            "Average / Incident",
            f"{average_users:,.0f}"
        )

    with col3:
        st.metric(
            "Maximum in One Incident",
            f"{maximum_users:,}"
        )

    # Resolution time
    st.subheader("⏱️ Incident Resolution Time")

    average_resolution = (
        df["Incident Resolution Time (in Hours)"].mean()
    )

    maximum_resolution = (
        df["Incident Resolution Time (in Hours)"].max()
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Average Resolution Time",
            f"{average_resolution:.2f} hours"
        )

    with col2:
        st.metric(
            "Maximum Resolution Time",
            f"{maximum_resolution} hours"
        )

    # Yearly financial loss
    st.subheader(
        "📈 Average Financial Loss by Year"
    )

    yearly_loss = (
        df.groupby("Year")[
            "Financial Loss (in Million $)"
        ]
        .mean()
    )

    st.line_chart(yearly_loss)


# ============================================================
# SECURITY ANALYSIS PAGE
# ============================================================

elif page == "🔐 Security Analysis":

    st.header("🔐 Security Analysis")

    st.write(
        """
        This section analyzes security vulnerabilities, attack
        sources and defense mechanisms used in the incidents.
        """
    )

    # Vulnerabilities
    st.subheader(
        "⚠️ Security Vulnerability Types"
    )

    vulnerability_counts = (
        df["Security Vulnerability Type"]
        .value_counts()
    )

    st.bar_chart(vulnerability_counts)

    # Attack sources
    st.subheader("🕵️ Attack Sources")

    source_counts = (
        df["Attack Source"]
        .value_counts()
    )

    st.bar_chart(source_counts)

    # Defense mechanisms
    st.subheader(
        "🛡️ Defense Mechanisms Used"
    )

    defense_counts = (
        df["Defense Mechanism Used"]
        .value_counts()
    )

    st.bar_chart(defense_counts)

    # Vulnerability vs attack type
    st.subheader(
        "🔥 Security Vulnerability vs Attack Type"
    )

    vulnerability_attack = pd.crosstab(
        df["Security Vulnerability Type"],
        df["Attack Type"]
    )

    st.dataframe(
        vulnerability_attack,
        use_container_width=True
    )


# ============================================================
# MACHINE LEARNING PREDICTION PAGE
# ============================================================

elif page == "🤖 ML Prediction":

    st.header("🤖 Cyberattack Type Prediction")

    st.write(
        """
        Enter information about a cyber incident.
        The trained Random Forest machine-learning model
        will predict the attack type.
        """
    )

    st.divider()

    # Input fields
    col1, col2 = st.columns(2)

    with col1:

        country = st.selectbox(
            "Country",
            sorted(df["Country"].unique())
        )

        year = st.number_input(
            "Year",
            min_value=2015,
            max_value=2024,
            value=2024
        )

        industry = st.selectbox(
            "Target Industry",
            sorted(df["Target Industry"].unique())
        )

        financial_loss = st.number_input(
            "Financial Loss (in Million $)",
            min_value=0.0,
            max_value=100.0,
            value=50.0
        )

        affected_users = st.number_input(
            "Number of Affected Users",
            min_value=0,
            max_value=1000000,
            value=500000
        )

    with col2:

        attack_source = st.selectbox(
            "Attack Source",
            sorted(df["Attack Source"].unique())
        )

        vulnerability = st.selectbox(
            "Security Vulnerability Type",
            sorted(
                df["Security Vulnerability Type"].unique()
            )
        )

        defense = st.selectbox(
            "Defense Mechanism Used",
            sorted(
                df["Defense Mechanism Used"].unique()
            )
        )

        resolution_time = st.number_input(
            "Incident Resolution Time (in Hours)",
            min_value=1,
            max_value=72,
            value=36
        )

    st.divider()

    # Prediction button
    if st.button(
        "🔮 Predict Attack Type",
        use_container_width=True
    ):

        try:

            # Load trained model
            model = joblib.load(
                "models/cyberattack_model.pkl"
            )

            # Create input DataFrame
            new_attack = pd.DataFrame({

                "Country": [country],

                "Year": [year],

                "Target Industry": [industry],

                "Financial Loss (in Million $)": [
                    financial_loss
                ],

                "Number of Affected Users": [
                    affected_users
                ],

                "Attack Source": [
                    attack_source
                ],

                "Security Vulnerability Type": [
                    vulnerability
                ],

                "Defense Mechanism Used": [
                    defense
                ],

                "Incident Resolution Time (in Hours)": [
                    resolution_time
                ]

            })

            # Make prediction
            prediction = model.predict(
                new_attack
            )[0]

            st.success(
                f"🎯 Predicted Attack Type: **{prediction}**"
            )

            # Prediction probabilities
            probabilities = (
                model.predict_proba(
                    new_attack
                )[0]
            )

            probability_df = pd.DataFrame({

                "Attack Type": model.classes_,

                "Probability": probabilities

            })

            probability_df = (
                probability_df
                .sort_values(
                    by="Probability",
                    ascending=False
                )
            )

            st.subheader(
                "📊 Prediction Probabilities"
            )

            st.dataframe(
                probability_df,
                use_container_width=True
            )

            # Probability chart
            st.bar_chart(
                probability_df,
                x="Attack Type",
                y="Probability"
            )

        except Exception as e:

            st.error(
                f"Prediction error: {e}"
            )