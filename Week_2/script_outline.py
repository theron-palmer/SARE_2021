#!/usr/bin/env python

def main(options):
    ens_gene_name = options.ens_gene_name
    gtf_file = options.gtf_file
    junc_bind_counts = options.junc_bind_counts

    # Your code should be written here

if __name__ == "__main__":

    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option("-e", "--ens_gene_name", dest="ens_gene_name",
                      help="The gene name to work with")
    parser.add_option("-g", "--gtf_file", dest="gtf_file",
                      help="The gtf file")
    parser.add_option("-j", "--junc_bind_counts", dest="junc_bind_counts",
                      help="The junction binder counts file")

    (options, args) = parser.parse_args()

    main(options)
