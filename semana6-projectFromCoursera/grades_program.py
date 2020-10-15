
import tkinter.filedialog
import functions_grade



a1_filename = tkinter.filedialog.askopenfilename()
a1_file= open(a1_filename,'r')


a1_histfilename = tkinter.filedialog.asksaveasfilename()
a1_histfile= open(a1_histfilename,'w')



## Read the grades into a list

grades =  functions_grade.read_grades(a1_file)


##Count the grades per range

range_counts = functions_grade.count_grade_ranges(grades)
print (range_counts)


##Write the histogram to the file
functions_grade.write_histogram(range_counts, a1_histfile)


##Close Files 
a1_file.close()
a1_histfile.close()



