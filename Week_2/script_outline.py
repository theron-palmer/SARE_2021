#!/usr/bin/env python

# What is this ^ for?

def main(options):
    # reading in the output file
    output_file = options.output_file
    
    # reading in the gtf file
    gtf_file = options.gtf_file
    print(type(gtf_file)) # what type() of python object is this?
    
    with open(output_file,'w') as out:
        # opening the gtf_file as a file object
        with open(gtf_file) as gtf:
            # doing things with the file opened

            # Parse each line of the .gtf into a list such that each line is one element in the list
            # There should be no newlines at the end of each element and this can be done in 1 to 2 lines of code
                # see functions read() and splitlines() for how to do this

            for line in gtf_list:
                # split the current line into another list (curr_list) based using the "\t" (tab) delimiter, see the split() function
                # split the last element in this list based on the ";" delimiter. store this in a variable, see the split() function

                # extract the chromosome, start location, end location, and strand from the line. store them in separate variables

                # if the line is a gene:
                    # extract the gene_id without quotations from the split last line variable
                    # see string.replace() for getting rid of the quotations
                    # form the gene_id line in string format
                    print(gene_id_line,file=out)
                # else if the line is a transcript:
                    # extract the transcript_id without quotations from the split last line variable
                    # see string.replace() for getting rid of the quotations
                    # form the transcript_id line in string format
                    print(transcript_id_line,file=out)

                   


if __name__ == "__main__":

    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option("-o", "--output_file", dest="output_file",
                      help="The output file to print to")
    parser.add_option("-g", "--gtf_file", dest="gtf_file",
                      help="The gtf file"))

    (options, args) = parser.parse_args()

    main(options)
