import streamlit as st


def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


st.set_page_config(page_title="Grade Manager", page_icon="🎓")
st.title("🎓 Grade Manager")

# Streamlit reruns this whole script on every interaction, so a plain list
# would be reset each time. session_state persists across reruns.
if "students" not in st.session_state:
    st.session_state.students = []

# ---------- Add-student form ----------
with st.form("add_student", clear_on_submit=True):
    name = st.text_input("Student name")
    mark = st.number_input(
        "Mark (0-100)", min_value=0.0, max_value=100.0, value=0.0, step=1.0
    )
    submitted = st.form_submit_button("Add student")

if submitted:
    name = name.strip()
    if not name:
        st.error("Please enter a student name.")
    elif mark < 0 or mark > 100:
        st.error("Invalid mark: please enter a number between 0 and 100.")
    else:
        st.session_state.students.append(
            {"Name": name, "Mark": mark, "Grade": get_grade(mark)}
        )
        st.success(f"Added {name}: {mark:g} ({get_grade(mark)})")

# ---------- Results ----------
students = st.session_state.students

st.subheader("Results")
if students:
    st.dataframe(students, use_container_width=True, hide_index=True)

    marks = [s["Mark"] for s in students]
    st.subheader("Class figures")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average", f"{sum(marks) / len(marks):.1f}")
    col2.metric("Highest", f"{max(marks):g}")
    col3.metric("Lowest", f"{min(marks):g}")

    if st.button("Clear all students"):
        st.session_state.students = []
        st.rerun()
else:
    st.info("No students yet. Add one using the form above.")