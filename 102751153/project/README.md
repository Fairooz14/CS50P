    # LUNAR PHASE TRACKER
    #### Video Demo:  <https://youtu.be/MYIlIdNA0qE>
    #### Description:
    The Lunar Phase Tracker is a Python-based project that enables users to determine the current lunar phase or the lunar phase for a specific date. The project includes several functions for calculating and displaying the phase of the Moon, making it a valuable tool for astronomers, stargazers, and anyone interested in tracking the moon's appearance in the night sky.

    ## Key Features
    Get the Current Date: The project provides a function to retrieve the current date, allowing users to quickly check the lunar phase for the present day.

#Calculate Lunar Phase: The project uses the ephem library to accurately calculate the lunar phase for a given date. The lunar phase is classified into four main phases: New Moon, First Quarter, Full Moon, and Last Quarter.

#Display Lunar Phase: Another function in the project displays the lunar phase in a human-readable format based on the numeric value calculated. For example, it converts a numeric value of 0 to "New Moon."

#Testability: The project incorporates a testing framework to ensure the accuracy of the lunar phase calculations and display functions. Test cases are included to verify that the code performs as expected.

     ## How does it works
     -The user runs the project, and it fetches the current date using Python's built-in date functions.

-The project then utilizes the ephem library to calculate the precise lunar phase for that date, mapping it to one of the four primary lunar phases.

-The calculated lunar phase is then displayed to the user in a human-readable format, such as "Full Moon" or "Last Quarter."

-The project's test framework validates the correctness of the lunar phase calculation and display functions, ensuring the accuracy of the project.