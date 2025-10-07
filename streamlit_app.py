import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd

# Sidebar with useful links
st.sidebar.title("Useful Links")
st.sidebar.markdown("[GoFundMe Page](https://bit.ly/QUBStepsToSweden)")
st.sidebar.markdown("[Participant Sign-up Form](https://bit.ly/s2s-signup)")
st.sidebar.markdown("[Distance Log (Participants Only)](https://bit.ly/s2s-distance-log)")
st.sidebar.markdown("[Donation Log (Participants Only)](https://bit.ly/s2s-donation-log)")

# Main page
st.set_page_config(layout="centered")

### UPDATE THESE VALUES ###
current_distance = 0  # km
current_donations = 0  # GBP

image = Image.open("Form Banner.png")
st.image(image, use_container_width=True)

donation_container = st.container()
distance_container = st.container()

with distance_container:
    st.header("Distance Progress")
    col1, col2 = st.columns([2,1], vertical_alignment="center")

    # Left column: Display fixed image
    with col1:
        image = Image.open("Dashboard - Map 1.png")
        st.image(image, use_container_width=True)

    # Right column: Display stats
    with col2:
        goal_distance = 2650  # km

        percent_complete = (current_distance / goal_distance) * 100

        st.metric(label="Goal Distance (km)", value=f"{goal_distance}")
        st.metric(label="Current Distance (km)", value=f"{current_distance}")
        st.metric(label="% of Goal Complete", value=f"{percent_complete:.1f}%")

        # Show any progress, even if less than 1%
        progress_value = percent_complete / 100
        if 0 < progress_value < 0.01:
            st.progress(0.01)
        else:
            st.progress(min(progress_value, 1.0))

with donation_container:
    st.header("Donation Progress")
    col3, col4 = st.columns([1,2], vertical_alignment="center")

    with col3:
        goal_donations = 5000  # GBP
        remaining_donations = goal_donations - current_donations

        percent_complete = (current_donations / goal_donations) * 100

        st.metric(label="Goal:", value=f"£{goal_donations}")
        st.metric(label="Raised:", value=f"£{current_donations}")

    with col4:
    # Pie chart data
        data = {
            "Status": ["Raised", "Remaining"],
            "Amount": [current_donations, remaining_donations]
        }

        # Create Plotly figure
        fig = px.pie(
            data,
            names="Status",
            values="Amount",
            color="Status",
            color_discrete_map={"Raised": "#7DC180", "Remaining": "#D5DBE0"},
            hole=0.5,  # makes it a donut chart (optional)
        )

        # Customise labels and title
        fig.update_traces(textinfo='percent+label', textfont_size=20)
        fig.update_layout(
            showlegend=False,
        )

        # Display in Streamlit
        st.plotly_chart(fig, use_container_width=True)

### LEADERBOARD SECTION ###
# leaderboard_container = st.container()
# with leaderboard_container:
#     st.header("Distance Leaderboard")
#     leaderboard_df = pd.read_csv("leaderboard.csv")
#     leaderboard_df = leaderboard_df.sort_values(by="Distance", ascending=False).reset_index(drop=True)

#     # Create Plotly bar chart
#     fig = px.bar(
#         leaderboard_df,
#         x="Distance",
#         y="Name",
#         orientation='h',  # Horizontal bars
#         text="Distance",  # Show distance on each bar
#         color="Distance",
#         color_continuous_scale="blugrn",
#         height=400
#     )

#     # Polish layout
#     fig.update_layout(
#         yaxis=dict(autorange="reversed"),  # Highest value on top
#         xaxis_title="Distance (km)",
#         yaxis_title=" ",
#         margin=dict(l=50, r=20, t=40, b=40),
#         coloraxis_showscale=False  # Hide color legend
#     )
#     fig.update_traces(textposition='outside')

#     # Display in Streamlit
#     st.plotly_chart(fig, use_container_width=True)

#     # names = leaderboard_df["Name"].tolist()
#     # places = list(range(1, len(names)+1))

#     # col_pos, col_name = st.columns([1,4])

#     # with col_pos:
#     #     for place in places:
#     #             st.markdown(
#     #                 f"""
#     #                 <div style="
#     #                     background-color:#f0f2f6;
#     #                     padding:10px;
#     #                     margin:5px 0;
#     #                     border-radius:8px;
#     #                     font-weight:bold;
#     #                     text-align:center;
#     #                 ">
#     #                     {place}
#     #                 </div>
#     #                 """, unsafe_allow_html=True
#     #             )


#     # with col_name:
#     #     for name in names:
#     #         st.markdown(
#     #             f"""
#     #             <div style="
#     #                 background-color:#f0f2f6;
#     #                 padding:10px;
#     #                 margin:5px 0;
#     #                 border-radius:8px;
#     #                 font-weight:bold;
#     #                 text-align:center;
#     #             ">
#     #                 {name}
#     #             </div>
#     #             """, unsafe_allow_html=True
#     #         )


st.caption("Page last updated: 7th October 2025")