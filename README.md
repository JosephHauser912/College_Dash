# College_Dash
Click [HERE](https://collegedash.onrender.com/) to view the dashboard

### From US News
University Information
State
College Name
Application Information
Tuition and Associated Cost Information
Faculty Information

### Specifications

Discover & visualize the dataset to get insights. Include some key visuals and written conclusions.
Report on relevant statistics.
Discuss your steps for cleaning the data.
Explain how you identify outliers and what you do with that information.
Explain how you approach missing values in the data.

### The Approach

I opened the dataset into a DataFrame using Jupyter Notebook to review the data and pull initial reports.
Once I was familiar with the data I used Dash Plotly to create an interactive dashboard that grouped and compared colleges by state.


### The Approach

Once the dataset was loaded into a notebook, 
it is best practice to review the contents to help familiarize yourself with the data and look for possible trends.

I used:
df.columns
df.describe()
df.dtypes


### Findings

Like any student, I was curious, which colleges were the most expensive. 
![Ten_expensive](https://github.com/JosephHauser912/College_Dash/assets/67341300/65a8f5fc-7a6f-40b9-908f-5b02977b8941)

With the top ten most expensive colleges in the country ruled out, I wanted to get more specific.
I wanted to find the highest Student-Faculty ratio. 

So why stop there? I defined two functions to return the max and min of each column so a student could narrow down their choices.

### Avg State Tuition
I averaged the in-state tuition for each state and used a hvplot to visualize.
This made it more clear the three most expensive states are: Vermont, Rhode Island, and Massachusetts.
The three least expensive states are: Wyoming, Utah, and North Dakota.
![State_avg_tuition](https://github.com/JosephHauser912/College_Dash/assets/67341300/3858c752-dea2-4c9e-a627-8d37ca7f9c84)

###Class Size and Tuition
Since a popular metric in school quality is class sizes, I wanted to look at the student-faculty ratio(SFR) by cost.
By looking at outliers in a scatter plot, it's easy to find outliers that have low tuition but high SFR. 
The standout for this metric is: The College of New Rochelle which is in the middle of the pack when it comes to tuition, but has a high SFR.
![SFR_tuition](https://github.com/JosephHauser912/College_Dash/assets/67341300/0eb5e98c-8015-4a47-a5da-fd2ebec76df7)



