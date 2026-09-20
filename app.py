import streamlit as st
from huggingface_hub import InferenceClient

# Page Setup
st.set_page_config(
    page_title="AI Code Review Assistant",
    page_icon="⚡",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    div[data-testid="stSidebar"] { background-color: #161B22; border-right: 1px solid #30363D; }
    .stButton>button {
        background: linear-gradient(90deg, #2563EB 0%, #7C3AED 100%);
        color: white; border: none; padding: 0.6rem 1rem; border-radius: 8px;
        font-weight: 600; width: 100%; transition: all 0.3s ease;
    }
    .stButton>button:hover { opacity: 0.9; transform: translateY(-1px); }
</style>
""", unsafe_allow_html=True)

# App Header
st.title("⚡ AI Code Review Assistant")
st.markdown("*Targeted pedagogical feedback powered by Hugging Face open-source LLMs.*")
st.divider()

# Sidebar Setup
st.sidebar.header("🔑 Configuration")
hf_token = st.sidebar.text_input("Hugging Face Access Token", type="password", help="Enter your 'hf_...' token.")

st.sidebar.header("🎯 Review Parameters")
language = st.sidebar.selectbox("Programming Language", ["Python", "Java", "C++", "JavaScript", "SQL", "C#"])
focus_area = st.sidebar.selectbox("Optimization Focus", ["Time Complexity", "Memory Usage", "Readability & Clean Code", "General Review"])

# Main Workspace
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("1. Source Code Input")
    user_code = st.text_area(
        "Paste the code snippet to inspect:",
        height=420,
        placeholder="def is_palindrome(data):\n    text = str(data)\n    return text == text[::-1]"
    )
    submit_btn = st.button("🚀 Analyze & Review Code", use_container_width=True)

with col2:
    st.subheader(f"2. Targeted Output: {focus_area}")
    
    if submit_btn:
        if not user_code.strip():
            st.error("⚠️ **Validation Error:** Please paste or type code before running the review.")
        elif not hf_token:
            st.error("⚠️ **Access Token Missing:** Please provide your Hugging Face token in the sidebar.")
        else:
            try:
                client = InferenceClient(token=hf_token)

                # Dynamic Prompt Builder based on selected focus area
                if focus_area == "Time Complexity":
                    prompt_focus = """Focus ONLY on Time Complexity.
Structure your response as follows:
## 1. Time Complexity Analysis (Big-O)
- Detailed breakdown of current runtime complexity.
## 2. Time Bottlenecks Identified
- Specific lines or loops causing time overhead.
## 3. Optimized Time Code
- Provide refactored code optimized strictly for speed.
## 4. Time Complexity Takeaway"""

                elif focus_area == "Memory Usage":
                    prompt_focus = """Focus ONLY on Memory & Space Complexity.
Structure your response as follows:
## 1. Space Complexity Analysis (Big-O)
- Detailed breakdown of current heap and stack memory usage.
## 2. Memory Inefficiencies Identified
- Specific variable allocations or data structures causing space overhead.
## 3. Memory-Optimized Code
- Provide refactored code optimized strictly for minimum memory footprint.
## 4. Memory Takeaway"""

                elif focus_area == "Readability & Clean Code":
                    prompt_focus = """Focus ONLY on Readability, Naming Conventions, and Code Hygiene.
Structure your response as follows:
## 1. Readability Assessment
- Analysis of naming, structure, and formatting.
## 2. Code Smells & Style Issues
- List non-idiomatic patterns or hard-to-read segments.
## 3. Clean Code Refactor
- Provide refactored code following standard style guidelines and clean naming.
## 4. Clean Code Takeaway"""

                else:  # General Review
                    prompt_focus = """Provide a complete general code review.
Structure your response as follows:
## 1. Overall Assessment
## 2. Inefficiencies & Anti-Patterns
## 3. Refactored Implementation
## 4. Educational Summary"""

                prompt = f"""You are an expert Pedagogical Code Review Assistant.
Strictly adhere to the requested focus area below. DO NOT output analysis outside of this scope.

Programming Language: {language}
Selected Focus: {focus_area}

Code:
{user_code}

Instructions:
{prompt_focus}
"""

                messages = [
                    {"role": "system", "content": "You are a precise coding tutor. You strictly follow formatting constraints and output ONLY the requested analysis focus without extra fluff."},
                    {"role": "user", "content": prompt}
                ]

                with st.spinner(f"Analyzing strictly for {focus_area}..."):
                    response = client.chat_completion(
                        model="Qwen/Qwen2.5-Coder-32B-Instruct",
                        messages=messages,
                        max_tokens=1000,
                        temperature=0.2
                    )

                result_text = response.choices[0].message.content
                st.markdown(result_text)
                st.warning(
                    "🔒 **Guardrail Applied:** Suggestions are for educational reference only. "
                    "Review, test, and verify logic manually before integrating into your projects."
                )

            except Exception as e:
                st.error(f"❌ **Execution Error:** {str(e)}")
    else:
        st.info(f"👈 Select your parameters, paste your code, and click **Analyze & Review Code** to get a targeted {focus_area} report.")