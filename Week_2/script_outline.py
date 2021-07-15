#!/usr/bin/env python

# What is this ^ for?
# The line above the previous one says where in your environment to find the python executable. 

def main(options):
    # reading in the output file
    output_file = options.output_file
    #print(type(output_file))
    
    # reading in the gtf file
    gtf_file = options.gtf_file
    #print(type(gtf_file)) # what type() of python object is this?
    
    with open(output_file,'w') as out:
        #print(type(out))
        # opening the gtf_file as a file object
        with open(gtf_file) as gtf:
            # doing things with the file opened

            # Parse each line of the .gtf into a list such that each line is one element in the list
            # There should be no newlines at the end of each element and this can be done in 1 to 2 lines of code
                # see functions read() and splitlines() for how to do this
            gtf_all = gtf.read()
            gtf_list = gtf_all.splitlines()
            #print(gtf_list[0])
            #print(gtf_list[2])
            #print(type(gtf_all))
            #print(gtf_all)

            for line in gtf_list:
                # split the current line into another list (curr_list) based using the "\t" (tab) delimiter, see the split() function
                # split the last element in this list based on the ";" delimiter. store this in a variable, see the split() function
                #print(line)
                curr_list = line.split("\t")
                # print(curr_list)
                
                #chromosome is 0
                #Start at 3
                #Stop at 4
                #Strand is + (6)
                
                
                

                # extract the chromosome, start location, end location, and strand from the line. store them in separate variables
                
                print_statement = "%s\t%s\t%s\t%s\t%s"
                
                chromosome = curr_list[0]
                start_location = curr_list[3]
                stop_location = curr_list[4]
                strand = curr_list[6]

                # if the line is a gene:
                    # extract the gene_id without quotations from the split last line variable
                    # see string.replace() for getting rid of the quotations
                    # form the gene_id line in string format
                if curr_list[2] == "gene":
                    
     
                    gene_id_full = curr_list[8]
                    new_list = curr_list[8].split(';')
                    #print(new_list)
                    gene_id_list = new_list[0]
                    #print(gene_id_list)
                    gene_id_string = gene_id_list.split(" ")
                    #print(gene_id_string)
                    gene_id_true = gene_id_string[1]
                    #print(gene_id_true)
                    
                    gene_id_real = gene_id_true.replace('"',"")
                    #print(gene_id_real)
                    
                    print_statement_gene = print_statement%(chromosome, start_location, stop_location, strand, gene_id_real)
                    
                    print(print_statement_gene, file = out)
                
                elif curr_list[2] == "transcript":
                    gene_id_full = curr_list[8]
                    new_list_transcript = curr_list[8].split(';')
                    #print(new_list_transcript)
                    transcript_id_list = new_list_transcript[2]
                    #print(transcript_id_list)
                    transcript_id_new = transcript_id_list.split(" ")
                    #print(transcript_id_new)
                    transcript_id_true = transcript_id_new[2]
                    #print(transcript_id_true)
                    transcript_id_real = transcript_id_true.replace('"',"")
                    #print(transcript_id_real)
                    
                    print_statement_transcript = print_statement%(chromosome, start_location, stop_location, strand, transcript_id_real)
                    
                    print(print_statement_transcript, file = out)
                 
                    
                    
                    
                    
                  
                    
                    
                    
                #print(gene_id_line,file=out)
                # else if the line is a transcript:
                    # extract the transcript_id without quotations from the split last line variable
                    # see string.replace() for getting rid of the quotations
                    # form the transcript_id line in string format
                #print(transcript_id_line,file=out)

                   


if __name__ == "__main__":

    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option("-o", "--output_file", dest="output_file",
                      help="The output file to print to")
    parser.add_option("-g", "--gtf_file", dest="gtf_file",
                      help="The gtf file")

    (options, args) = parser.parse_args()

    main(options)
