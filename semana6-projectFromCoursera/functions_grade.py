def read_grades(gradefile):
    '''(file open for reading) -> list of float

    Read and return the list of grades in gradefile

    Precondiition: gradefile starts with a header with
    no blank lines, then has a blank line, and then lines
    containing a student number and grade
    '''
    ## skip the header
    line=gradefile.readline()
    
    while line != '\n':
        line=gradefile.readline()
          

    ## Read the grades, accumulating    them into a list
        
    grades=[]
    
    line= gradefile.readline()
    while line != '':
        
        grade = line[line.rfind(' ')+1:]
        grades.append(float(grade))
        line = gradefile.readline()
        
    return grades  
        
def count_grade_ranges(grades):
    '''(list of float) -> list of int

    Return a list of int where each index indicates how manu grades in these
    ranges:

    0-9 : index 0
    10-19: 1
    20-29 : 2
    :
    90-99: 9
    100: 10

    >>> count_grade_ranges ([77.5, 37.5, 0.5, 9.5, 72.5, 100.0 ,55.0 ,70.0 ,79.5])
    [2,0,0,1,0,1,0,4,0,0,1]

    '''

    range_counts = [0]*11

    for grade in grades:
        which_range = int(grade//10)
        range_counts[which_range]= range_counts[which_range] + 1

    return range_counts

def write_histogram(range_counts, histfile):
    '''(list of int, file open for writing ) -> NoneType

    Write a histogram of *'s based on the number of grades in each range

    Output format example:

    0-9:   
    10-19: 
    20-29: 
      :
    90-99: **
    100:   **
    '''

    histfile.write('0-9:   ')
    histfile.write('*' *  range_counts[0])
    histfile.write('\n')

    # write the 2-digits ranges
    for i in range(1,10):
        low = i *10
        high = i *10 +9
        histfile.write(str(low) + '-' + str(high) + ': ')
        histfile.write('*' *  range_counts[i])
        histfile.write('\n')


    histfile.write('100:   ')
    histfile.write('*' *  range_counts[-1])
    histfile.write('\n')
    
