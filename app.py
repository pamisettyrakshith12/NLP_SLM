import streamlit as st
import pandas as pd

from pdf_processor import (
    extract_text_from_pdf,
    extract_terms
)

from translator import translate_to_telugu


st.set_page_config(
    page_title="English → Telugu Glossary",
    page_icon="🌐",
    layout="wide"
)


# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    color: #666;
    margin-bottom: 30px;
}

.term-card {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="main-title">'
    '🌐 English → Telugu Glossary Translator'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Translate domain-specific English terminology into Telugu '
    'using a Small Language Model.'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("📄 Glossary Settings")

uploaded_file = st.sidebar.file_uploader(
    "Upload English Glossary PDF",
    type=["pdf"]
)

context = st.sidebar.selectbox(
    "Select Context",
    [
        "Computer Science",
        "Electronics",
        "Medicine",
        "Business",
        "General"
    ]
)

st.sidebar.info(
    "The selected context helps maintain "
    "domain-specific terminology."
)


# -----------------------------
# Main
# -----------------------------

if uploaded_file:

    if st.button(
        "🔄 Extract Glossary",
        type="primary"
    ):

        with st.spinner("Reading PDF..."):

            text = extract_text_from_pdf(
                uploaded_file
            )

            terms = extract_terms(text)

            st.session_state["terms"] = terms

    if "terms" in st.session_state:

        terms = st.session_state["terms"]

        st.success(
            f"{len(terms)} glossary entries extracted."
        )

        st.subheader("📖 English Glossary")

        english_data = pd.DataFrame(
            terms
        )

        st.dataframe(
            english_data,
            use_container_width=True
        )


        # -----------------------------
        # Translation
        # -----------------------------

        if st.button(
            "🚀 Translate to Telugu",
            type="primary"
        ):

            translated_terms = []

            progress = st.progress(0)

            for i, item in enumerate(terms):

                english_term = item["term"]
                english_definition = item["definition"]

                telugu_term = translate_to_telugu(
                    english_term
                )

                telugu_definition = translate_to_telugu(
                    english_definition
                )

                translated_terms.append({

                    "English Term":
                        english_term,

                    "English Definition":
                        english_definition,

                    "Telugu Term":
                        telugu_term,

                    "Telugu Definition":
                        telugu_definition

                })

                progress.progress(
                    (i + 1) / len(terms)
                )


            st.session_state[
                "translated"
            ] = translated_terms


        # -----------------------------
        # Results
        # -----------------------------

        if "translated" in st.session_state:

            st.subheader(
                "🇮🇳 Telugu Translation"
            )

            translated_df = pd.DataFrame(
                st.session_state["translated"]
            )

            st.dataframe(
                translated_df,
                use_container_width=True
            )


            # -----------------------------
            # Individual Results
            # -----------------------------

            st.subheader(
                "🔍 Translation Preview"
            )

            for item in st.session_state["translated"]:

                with st.container():

                    st.markdown(
                        f"### {item['English Term']}"
                    )

                    st.write(
                        "**Telugu:** "
                        + item["Telugu Term"]
                    )

                    st.write(
                        "**English:** "
                        + item["English Definition"]
                    )

                    st.write(
                        "**Telugu:** "
                        + item["Telugu Definition"]
                    )

                    st.divider()


            # -----------------------------
            # Download
            # -----------------------------

            csv = translated_df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                label="⬇ Download Telugu Glossary",
                data=csv,
                file_name="telugu_glossary.csv",
                mime="text/csv"
            )


else:

    st.info(
        "👈 Upload an English glossary PDF "
        "from the sidebar to begin."
    )