# import streamlit as st
# from camel_agents.subject_classifier import classify_subject
# from camel_agents.subject_agents import get_agent_by_subject


# st.set_page_config(
#     page_title="AI Tutor (Camel + Mistral)",
#     layout="centered",
#     page_icon="🧠",
#     initial_sidebar_state="expanded"
# )


# st.markdown("""
#     <style>
#         .stTextInput input {
#             padding: 12px !important;
#             border-radius: 10px !important;
#         }
#         .stSpinner > div {
#             text-align: center;
#         }
#         .success-box {
#             padding: 12px;
#             background-color: #2d3748;
#             color: white !important;
#             border-radius: 10px;
#             border-left: 5px solid #4CAF50;
#             margin: 10px 0;
#         }
#         .answer-box {
#             padding: 20px;
#             background-color: #2d3748;
#             color: white !important;
#             border-radius: 10px;
#             margin: 15px 0;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         }
#         .answer-box p, .answer-box li, .answer-box code,
#         .success-box p, .success-box li {
#             color: white !important;
#         }
#         .title-text {
#             font-size: 2.5rem !important;
#             text-align: center;
#             margin-bottom: 30px !important;
#         }
#         /* Make sure markdown text is visible */
#         .stMarkdown, .stMarkdown p, .stMarkdown li {
#             color: white !important;
#         }
#     </style>
# """, unsafe_allow_html=True)


# st.markdown('<h1 class="title-text">📚 AI Tutor — Multi-Agent System</h1>', unsafe_allow_html=True)
# st.markdown("""
#     <div style="text-align: center; margin-bottom: 30px; color: #666;">
#         Powered by CAMEL-AI + Mistral | Ask any subject-related question
#     </div>
# """, unsafe_allow_html=True)


# query = st.text_input(
#     "",
#     placeholder="Ask your question here... (e.g. Explain quantum physics, Solve this math problem...)",
#     key="query_input"
# )

# if query:
#     with st.spinner("🔍 Routing your query to the right subject expert..."):
#         subject = classify_subject(query)
    
#     if subject:
#         st.markdown(f"""
#             <div class="success-box">
#                 <b>🧭 Routed to:</b> <span style="color: #4CAF50;">{subject.capitalize()} Expert</span>
#             </div>
#         """, unsafe_allow_html=True)
        
#         agent_fn = get_agent_by_subject(subject)
#         if agent_fn:
#             with st.spinner(f"💭 {subject.capitalize()} expert is analyzing your question..."):
#                 response = agent_fn(query)
            
#             st.markdown("### 🎯 Answer")
#             st.markdown(f'<div class="answer-box">{response}</div>', unsafe_allow_html=True)
            

#             st.markdown("<br><br>", unsafe_allow_html=True)
#         else:
#             st.error("❌ Sorry, no expert is available for this subject yet.")
#     else:
#         st.error("❌ Unable to determine the subject area. Please try rephrasing your question.")


# with st.sidebar:
#     st.markdown("## ℹ️ About")
#     st.markdown("""
#         This AI Tutor uses a multi-agent system with:
#         - **CAMEL-AI** for agent coordination
#         - **Mistral** for language understanding
#         - **Specialized agents** for different subjects
#     """)
    
#     st.markdown("## 📚 Supported Subjects")
#     st.markdown("""
#         - Mathematics
#         - Science
#         - History
#         - Literature
#         - Programming
#         - And more...
#     """)
    
#     st.markdown("## 💡 Tips")
#     st.markdown("""
#         - Be specific with your questions
#         - For complex topics, break them down
#         - The more precise you are, the better the answer
#     """)












import streamlit as st
from camel_agents.subject_classifier import classify_subject
from camel_agents.subject_agents import get_agent_by_subject

st.set_page_config(
    page_title="AI Tutor (Camel + Mistral)",
    layout="centered",
    page_icon="🧠",
    initial_sidebar_state="expanded"
)

# Updated CSS with slightly smaller fonts
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        .title-text {
            font-size: 2.8rem !important;
            font-weight: 600 !important;
            color: #ffffff;
            text-align: center;
            line-height: 1.5;
            margin-top: 2rem;
            margin-bottom: 1.5rem;
        }

        .stTextInput input {
            padding: 14px !important;
            font-size: 1.2rem !important;
            border-radius: 12px !important;
        }

        .stSpinner > div {
            text-align: center;
            font-size: 1.1rem !important;
        }

        .success-box {
            padding: 16px;
            background-color: #2d3748;
            color: white !important;
            border-radius: 12px;
            border-left: 6px solid #4CAF50;
            margin: 16px 0;
            font-size: 1.1rem !important;
        }

        .answer-box {
            padding: 20px;
            background-color: #2d3748;
            color: white !important;
            border-radius: 12px;
            margin: 20px 0;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
            font-size: 1.2rem !important;
        }

        .stMarkdown, .stMarkdown p, .stMarkdown li {
            color: white !important;
            font-size: 1.1rem !important;
        }

        /* Sidebar font */
        .css-1d391kg {
            font-size: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Heading
st.markdown("""
    <h1 class="title-text">Welcome, Tushar 👋</h1>
    <h3 style="text-align: center; font-weight: 400; color: #ccc; line-height: 1.6;">
        Multi-agent AI at your service. Ask anything.
    </h3>
""", unsafe_allow_html=True)

# Subheading


# Text input
query = st.text_input(
    "",
    placeholder="Ask your question here... (e.g. Explain quantum physics, Solve this math problem...)",
    key="query_input"
)

# Logic
if query:
    with st.spinner("🔍 Routing your query to the right subject expert..."):
        subject = classify_subject(query)

    if subject:
        st.markdown(f"""
            <div class="success-box">
                <b>🧭 Routed to:</b> <span style="color: #4CAF50;">{subject.capitalize()} Expert</span>
            </div>
        """, unsafe_allow_html=True)

        agent_fn = get_agent_by_subject(subject)
        if agent_fn:
            with st.spinner(f"💭 {subject.capitalize()} expert is analyzing your question..."):
                response = agent_fn(query)

            st.markdown("### 🎯 Answer")
            st.markdown(f'<div class="answer-box">{response}</div>', unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
        else:
            st.error("❌ Sorry, no expert is available for this subject yet.")
    else:
        st.error("❌ Unable to determine the subject area. Please try rephrasing your question.")

    st.markdown("""
    <div style="text-align: center; margin-bottom: 25px; color: #aaa; font-size: 1.05rem;">
        Powered by CAMEL-AI + Mistral
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ℹ️ About")
    st.markdown("""
        This AI Tutor uses a multi-agent system with:
        - **CAMEL-AI** for agent coordination  
        - **Mistral** for language understanding  
        - **Specialized agents** for different subjects
    """)
    st.markdown("## 📚 Supported Subjects")
    st.markdown("""
        - Mathematics  
        - Science  
        - History  
        - Literature  
        - Programming  
        - And more...
    """)
    st.markdown("## 💡 Tips")
    st.markdown("""
        - Be specific with your questions  
        - For complex topics, break them down  
        - The more precise you are, the better the answer
    """)
    
