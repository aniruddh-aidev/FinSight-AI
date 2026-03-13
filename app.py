import streamlit as st
from crew import run_crew

st.set_page_config(
    page_title="FinSight AI",
    page_icon="📈",
    layout="centered"
)

st.markdown("""
    <h1 style='text-align: center; color: #00C896;'>📈 FinSight AI</h1>
    <p style='text-align: center; color: gray;'>AI-powered market research tool — for informational purposes only</p>
    <hr>
""", unsafe_allow_html=True)

st.markdown("### 🔍 Enter a Stock or Sector to Analyze")

sector = st.text_input(
    label="",
    placeholder="e.g. Oil and Gas, Technology, AAPL, TSLA..."
)

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    analyze = st.button("🚀 Analyze", use_container_width=True)

if analyze:
    if not sector:
        st.warning("Please enter a stock or sector first!")
    else:
        try:
            with st.spinner("🤖 Agents are working... This may take a few minutes."):
                result = run_crew(sector)
            st.success("✅ Analysis Complete!")
            st.markdown("---")
            st.markdown("## 📊 Investment Report")
            st.markdown(str(result))
            st.markdown("---")
            st.caption("⚠️ FinSight AI is a research assistance tool only. The analysis provided is not financial advice. We are not responsible for any investment decisions, transactions, or financial losses made using this tool. Always conduct your own research before investing.")
        except Exception as e:
            if "rate_limit" in str(e).lower():
                st.error("⏳ Rate limit reached. Please wait a minute and try again.")
            elif "access denied" in str(e).lower():
                st.error("🌐 Network error. Please check your internet connection or try a hotspot.")
            else:
                st.error(f"Something went wrong: {str(e)}")