import streamlit as st 
from env import StudyEnv
from agent import StudyAgent

# styling
st.markdown(""" 
<style>
            .stApp{
            background: linear-gradient(to right,#403b4a,#e7e9bb);
            color : white;
            }
</style>            
""",unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center;color:#FFD700;'>📚 AI SELF-LEARNING STUDY PLANNER 🚀</h1> ",
            unsafe_allow_html=True)

# User input
hours = st.slider("select study hours", 1, 10, 6)

subjects_input = st.text_input("enter subjects (comma seprated)",'physics , biology')

subjects = [s.strip() for s in subjects_input.split(',')]


if "plan" not in st.session_state:
    st.session_state.plan = None

if 'checked' not in st.session_state:
    st.session_state.checked = {}


# button logic
st.markdown(
    """
<style>
div.stButton > button{
background-color: #ff4b2b;
color: white;
border-radius:10px;
height: 3em;
width: 100%;
}
</style>
""",unsafe_allow_html=True
)

if st.button("Generate Plan"):
    env = StudyEnv()
    agent = StudyAgent()

    env.state = {
        "hours_available": hours,
        "subjects": subjects,
        "completed": []
    }

    state = env.get_state()
    action = agent.get_action(state)

    st.session_state.plan = action['plan']
    st.session_state.checked = {}

# display logic
    
if st.session_state.plan:   
    st.subheader("📑 STUDY PLAN")

    completed_tasks = []

    for sub, hr in st.session_state.plan.items():
        key = f"{sub}"
        checked = st.checkbox(f"{sub} -> {hr} hrs", key=key)


        if checked:
            completed_tasks.append(sub)

# score system
    score =len(completed_tasks)/len(st.session_state.plan)

    st.subheader("🎯 Score")
    st.write(f"{score * 100:.2f}% completed")

# progress logic

    st.subheader('📊 PROGRESS')
    st.text('Complete Subjects : '+ str( completed_tasks))
    st.write("score : ", float(score))
    st.info("💡 AI Suggestion : Focus on more on weak subjects for better score")
#rank system

    if score == 1:
        st.success("🏆 Excellent")
    elif score >= 0.7:
        st.info("👍 Good")
    elif score >= 0.4:
        st.warning("⚠ Need Improvement")
    else:
        st.error("❌ Poor ! Focus more !")
