import csv # not used 
import pandas as pd
import argparse
import os
import matplotlib.pyplot as plt
#importing modules used in the script that is not in prepared in base python

def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path
#script given by teachers, checks as stated in the field if the given file, which is given using 
#argparse is a file to begin with 

def hist(data):
    z = data
    #defining data as variable z 
    plt.hist(z)
    #plotting a matplotlib histogram using said defined variable
    plt.title("Distribution of gene expression")
    #adding title
    plt.xlabel("Expression")
    #add name for the x axis label
    plt.ylabel("Number of genes")
    #add name for the y axis label
    plt.savefig('fpkm_distribution.png')
    #saving figure as png under the name fpkm_distribution
    plt.show()
    #shows how the figure looks in a temporary screen and also closes down the plot 
#function for making, clarifying with labels and saving a histogram plot 


def main():
    # Capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Process a string and a folder.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Input a csv file')
    args = parser.parse_args()
    # Is done with the specified flags followed by the path to the file, in this case the file is in the same directory as 
    # as the code so the filename is sufficient, if the function for checking if it is a file is unwanted also 
    # remove", type=existing_file, required=True" and only specified using flags but this works 
    # finally this is also made by the teachers 


    numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]
    #importing given numbers as a list

    k = 0
    for n in numbers:
        if abs(n) >= abs(10):
            k += n
        else:
            continue
    print(k)
    # a for loop checking if the value of the list is the absolute value of 10 or larger 
    # if so it is adding them to an intger so as to get the sum of if those values then printing those
    # of not is that k intger used for summing up all the values must be made beforehande

    j = []
    for n in numbers:
        h = 0
        if n < 0:
            h += (n*n*n)
            j.append(h)
        else:
             continue
    print(j)
    # a for loop that chekis if the number in the list is smaller than 0 and if so cubing them 
    #then adding said resultig cubed value to a list, making a list of all negative valued cubed
    #the printing said list, of note is that the list should be prepared beforehand which is done using j here

    dupes = set()
    seen = set()
    mk =[] 
    h = 0 
    for n in numbers:
        if abs(n) in seen:
            h += 1
            dupes.add(n)
            mk.append(abs(n))
        else:
            seen.add(n)
    print(f'first dupe {mk[0]}' if h != 0 else print("No repeats"))
    # a for loop and print commande checking the list for duplicates and if one or more cuplicates is found
    # printing a message contaning the first absolute repeated number this is done by making the sets that are then 
    #checked for all numbers and if there is a repeating absolute number said absolute number is added to the premade list
    #Also added to is one number to an integer for each repeating number to a integer made outside the fore loop
    #which is used in the pring to check if there is a repeated number, if there is none "No repeats" is pringted


    df = pd.read_csv('brca_head500_genes.csv', sep=',')
    #taking the file inputted by argparse specified using a flag in terminal and reading it as a 
    #dataframe using pandas while aslo making sure as to not miss mentionning that the given data is comma separated
    print(df)
    #checking to see if import worked by checking the content of the created dataframe 

    hist(df['fpkm_log2'])
    #calling function that plots saves and annotates a histogram of note is that the coloumn studied
    #should included so call the dataframe then the which column is wanted inside of the dataframe



if __name__ == "__main__":
    main()
#safety function, made by teachers, make sure the code imports do get anything weird
#meaning that only when the script is ran does the functions activate, not when the function is imported