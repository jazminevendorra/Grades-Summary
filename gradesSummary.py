# This program will generate a course grades summary report based on the
#course, instructor, and student data stored in a file.
#
# Unit 6 Assignment

def main():
    # Intro
    print("Course Grades Summary Report ...")

    tryAgain = 'y'

    while tryAgain == 'y':
        # Ask for name of file
        file = input("\nEnter name of course file: ")

        # if correct file
        if (file == 'COP1000C.txt'):
            # Initialize variables
            failed = 0
            passed = 0
            count = 0
            grades_sum = 0
            
            # Open the file for reading.
            course_file = open('COP1000C.txt','r')

            # Read course number and description
            num_and_description = course_file.readline()
            num_and_description = num_and_description.rstrip('\n')

            # Read professor's name
            prof = course_file.readline()
            prof = prof.rstrip('\n')

            # Read term
            term = course_file.readline()
            term = term.rstrip('\n')

            # Display File information
            print("\n------------------------------------------------------------")
            print("\t\tBroward College Grades Summary")
            print("------------------------------------------------------------\n")
            print(num_and_description)
            print('Professor:', prof,'\t\tTerm:',term)
            print("\nStudent Name\t\t\tGrade")
            print("----------------------------------------")
           
            # Read first line to test for empty string
            name = course_file.readline()

            # Get rid of \n
            name = name.rstrip('\n')

            # If no empty string
            while name != '':
                grade = course_file.readline()

                # Convert grade to an int
                grade = int(grade)

                # Print name and grade
                print(format(name,'20'),format(grade,'15'))

                # Passing or failing count
                if grade < 60:
                    failed = failed +1
                else:
                    passed += 1

                # Total students
                count += 1

                #Grade count
                grades_sum += grade

                # Passing percent calc
                pass_percent = (passed * 100)/count
                
                # Average grade
                avg_grade = grades_sum/count
                
                name = course_file.readline()
                name = name.rstrip('\n')

                
            # Display strudent performance (passed, failed, pass percent, and average grade)
            print("\nStudents' Performance")
            print("----------------------------------------")
            print('Passed:',passed,'\t\tFailed:', failed)
            print('Passing Percent:',format(pass_percent,'.0f'),'%')
            print('Average Grade:',format(avg_grade,'.0f'))
            
            #Close file
            course_file.close()

        else:
            print("Error ...", file, "file not found.")

        # Ask if user wants to process another file
        tryAgain = input("\nWould you like to process another file (y/n)? ")

# Call main
main()
