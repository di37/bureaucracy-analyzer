import streamlit as st

from bureaucracy import HRDepartment, FinanceDepartment, BureaucracyAnalyzer
from utilities import initialize_session_state


def main():
    st.title("Bureaucracy Analyzer")

    initialize_session_state()

    # Sidebar for department selection
    st.sidebar.title("Select Department")
    department_choice = st.sidebar.selectbox(
        "Choose a department", ["Human Resources", "Finance"]
    )

    # Update department if selection changes
    if (
        st.session_state.department is None
        or st.session_state.department.name != department_choice
    ):
        if department_choice == "Human Resources":
            st.session_state.department = HRDepartment()
        else:
            st.session_state.department = FinanceDepartment()
        st.session_state.current_question_index = 0
        st.session_state.answers = {}

    department = st.session_state.department

    # Display the current question
    if st.session_state.current_question_index < len(department.questions):
        st.subheader(f"Question for {department.name} Department:")
        current_question = department.questions[st.session_state.current_question_index]
        st.write(current_question)

        # Use a form to handle the answer submission
        with st.form(key=f"question_form_{st.session_state.current_question_index}"):
            user_answer = st.text_area("Your answer:", height=100)
            submit_button = st.form_submit_button("Next Question")

        if submit_button:
            if user_answer:
                st.session_state.answers[current_question] = user_answer
                st.session_state.current_question_index += 1
                st.rerun()
            else:
                st.warning(
                    "Please provide an answer before moving to the next question."
                )

    else:
        st.subheader("Analysis Results")
        if st.button("Analyze Bureaucracy"):
            # Transfer answers to the department object
            for question, answer in st.session_state.answers.items():
                department.set_response(question, answer)

            analyzer = BureaucracyAnalyzer()
            analysis_placeholder = st.empty()
            code_placeholder = st.empty()

            full_response = ""
            for chunk in analyzer.analyze_stream(department):
                full_response += chunk.text
                analysis_placeholder.markdown(full_response)

            code_placeholder.code(full_response, language="markdown")

        if st.button("Start Over"):
            st.session_state.current_question_index = 0
            st.session_state.department = None
            st.session_state.answers = {}
            st.rerun()


if __name__ == "__main__":
    main()
