import streamlit as st
from multiapp import MultiApp
from apps import home, courses, instructors, add_instructor, add_lesson

app = MultiApp()

# Add all your applications here
app.add_app("Home", home.app)
app.add_app("Courses", courses.app)
app.add_app("Instructors", instructors.app)
app.add_app("Add Instructor", add_instructor.app)
app.add_app("Add Lesson", add_lesson.app)

# The main app
app.run()
