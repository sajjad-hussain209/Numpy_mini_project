import numpy as np


data = np.loadtxt(
    "student-mat.csv",
    delimiter=";",
    skiprows=1,
    usecols=(13, 29, 30, 31, 32),
    quotechar='"',
)
# print(data)
g3 = data[:,4] #grade 3 indexing
g2 = data[:,3] #grade 2 indexing
g1 = data[:,2] #grade 1 indexing
print("====================================================================================================")
print("====================================Average comparison of grades====================================")
print("G1 average:", np.mean(g1))
print("G2 average:", np.mean(g2))
print("G3 average:", np.mean(g3))
change_12 = np.mean(g2) - np.mean(g1)
change_23 = np.mean(g3) - np.mean(g2)
print("Change from G1 to G2:", change_12)
print("Change from G2 to G3:", change_23)
if(change_12>0):
    print("There is an increase from G1 to G2")
elif(change_12<0):
    print("There is a decrease from G1 to G2")
else:
    print("There is no change in the mean.")
if(change_23>0):
    print("There is an Increase from G2 to G3")
elif (change_23<0):
    print("There is a decrease from G2 to G3")
else: 
    print("There is no change in the mean.")


print("G1 median:", np.median(g1))
print("G2 median:", np.median(g2))
print("G3 median:", np.median(g3))

print("Minimum value in G3: ", g3.min())
print("Minimum value in G2: ", g2.min())
print("Minimum value in G1: ", g1.min())

# study time vs grade 3
print("=============================================================================")
print("============================study time vs grade 3============================")
st_time = data[:, 0]
s1 = np.mean(g3[st_time==1])
s2 = np.mean(g3[st_time==2])
s3 = np.mean(g3[st_time==3])
s4 = np.mean(g3[st_time==4])
averages = np.array([s1, s2, s3, s4])

highest_index = np.argmax(averages)
highest_category = highest_index + 1

print("Study-time category with highest average:", highest_category)
print("Highest average G3:", averages[highest_index])
print("Average for category 1", s1)
print("Average for category 2", s2)
print("Average for category 3", s3)
print("Average for category 4", s4)
for i in range(1, 5):
    count = np.sum(st_time == i)
    print(f"Students in category {i}: {count}")
if(s2-s1>0):
    print("There is an increase in the grade of students who study for 2 hrs instead of 1hr.")
elif(s2-s1<0):
    print("There is an decrease in the grade of students who study for 2 hrs instead of 1hr.")
if(s4-s3>0):
    print("There is an increase in the grade of students who study for 4 hrs instead of 3hr.")
elif(s4-s3<0):
    print("There is an decrease in the grade of students who study for 4 hrs instead of 3hr.")

# passing students
passing = np.sum(g3>=10)
failing =  np.sum(g3<10)
total_students = len(g3)
pass_per = (passing/total_students)*100
fail_per = (failing/total_students)*100
print("===================================================================")
print("===================Passing/failing students data===================")
print("Number of passing students in final grades: ", passing)
print("Number of failiing students in final grades: ", failing)
print("percentage of passing students: ", pass_per)
print("percentage of failing students: ", fail_per)
#  improved student calculations
improved = g3 > g1
decreased = g3 < g1
unchanged = g3 == g1

imp_count = np.sum(improved)
dec_count = np.sum(decreased)
same_count = np.sum(unchanged)

per_imp = (imp_count / total_students) * 100
per_dec = (dec_count / total_students) * 100
per_same = (same_count / total_students) * 100
print("==================================================")
print("==============Individual performance==============")

print("Students who improved:", imp_count)
print("Improvement percentage:", per_imp)

print("Students who decreased:", dec_count)
print("Decrease percentage:", per_dec)

print("Students unchanged:", same_count)
print("Unchanged percentage:", per_same)
# # absense time
absences = data[:, 1]
ranges = [
    (0, 0),
    (1, 5),
    (6, 10),
    (11, 15),
    (16, 20),
    (21, 25),
    (26, 30),
    (31, 35),
    (36, 40),
    (41, 45),
    (46, 50),
    (51, 55),
    (56, 60),
    (61, 65),
    (66, 70),
    (71, 75)
]
print("===================================================")
print("==============absense vs grade effect==============")
for low, high in ranges:
    grades = g3[(absences >= low) & (absences <= high)]

    if len(grades) > 0:
        print(low, "-", high, "Mean:", np.mean(grades))
    else:
        print(low, "-", high, "No students")

