''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv
def main():

# create a file object to open the file in read mode
outfile = open('students.csv', 'r')



# create a csv object from the file object
gpa = csv.reader(outfile, delimiter=',')

#skip the header row
next(gpa)

#create an outfile object for the pocessed record

outfile = 

#create a new dictionary named 'student_dict'
student_dict = open('students.csv', 'w')

for record in student_dict:
    gpa = record[0]
    stud_id = record[8]





student_dict = {stud_id,pin,firstname,lastname,city,state,major,classification,gpa,
123456789,1111,homer,wells,seattle,wa,mis,fr,3.00,
124567890,2121,bob,norbert,bothell,wa,fin,jr,2.70,
234567890,3321,candy,kendall,tacoma,wa,acct,jr,3.50,
345678901,1141,wally,kendall,seattle,wa,mis,sr,2.80,
456789012,2333,joe,estrada,seattle,wa,fin,sr,3.20,
567890123,0021,mariah,dodge,seattle,wa,mis,jr,3.60,
678901234,2344,tess,dodge,redmond,wa,acct,so,3.30,
789012345,2212,roberto,morales,seattle,wa,fin,jr,2.50,
876543210,0021,cristopher,colan,seattle,wa,mis,sr,4.00,
890123456,2344,luke,brazzi,redmond,wa,mis,sr,2.20,
901234567,2212,william,pilgram,seattle,wa,mis,so,3.80}

print(type(student_dict))


print(student_dict)


#use a loop to iterate through each row of the file

    #check if the GPA is below 3.0. If so, write the record to the outfile

	for gpa in student_dict:
	    print(gpa)
	    print(student_dict[gpa])



    # append the record to the dictionary with the student id as the Key

print(student_dict)
stud_id[''] = 
print(student_dict)


    # and the value as the GPA
    
print(student_dict)
gpa[''] = 
print(student_dict)




#print the entire dictionary

print(student_dict)

#Print the student id 
print(stud_id)

#print out the corresponding GPA from the dictionary

print(gpa)

#close the outfile


    outfile.close()
main()
