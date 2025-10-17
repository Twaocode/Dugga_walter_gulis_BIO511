import csv 
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
    df = pd.read_csv('brca_head500_genes.csv', sep=',')
    z = df['fpkm_log2']
    plt.hist(z)
    plt.title("Distribution of gene expression")
    plt.xlabel("Expression")
    plt.ylabel("Number of genes")
    plt.savefig('fpkm_distribution.png')
    plt.show()
#function for making, clarifying with labels and saving a histogram plot 


def main():
    # Capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Process a string and a folder.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Input a csv file')
    args = parser.parse_args()
    # Is done with the specified flags followed by the path to the file, in this case the file is in the same directory as 
    # as the code so the filename is sufficient 

    numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]
    k = 0

    for n in numbers:
        if abs(n) >= abs(10):
            k += abs(n)
        else:
            continue
    print(k)
    # a for loop checking if the value of the list is the absolute value of 10 or larger 
    # if so it is adding them to an intger so as to get the sum of if those values then printing those

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
    #the printing said list, of note is that the list should be prepared beforehand 

    dupes = set()
    seen = set()
    mk =[] 
    k = 0 
    for n in numbers:
        if abs(n) in seen:
            k += 1
            dupes.add(n)
            mk.append(abs(n))
        else:
            seen.add(n)
    print(f'first dupe {mk[0]}' if k != 0 else print("No dupes"))
    # a for loop and print commande checking the list for duplicates and if one or more cuplicates is found
    # printing a message contaning the first absolute repeated number this is done by making the sets that are then 
    #checked for all numbers and if there is a repeating absolute number said absolute number is added to the premade list
    #Also added to is one number to an integer for each repeating number to a integer made outside the fore loop
    #which is used in the pring to check if there is a repeated number, if there is none "No repeats" is pringted


    df = pd.read_csv('brca_head500_genes.csv', sep=',')
    #print(df)
    z = df['fpkm_log2']
    hist(z)




            

    





if __name__ == "__main__":
    main()