# Genomic coordinates and the Gene transfer format

## Part 1

The human genome can be viewed within a document as a string of nuceotide bases from start to end. To determine any worthwhile information about the human genome, its sequence of nucleotide bases must be viewed with respect to its chromosomes, genes, introns, and exons amongst other things. Through experimentation, the locations of chromosomes, genes, introns, and exons have been documented and are updated as improved versions of the human genome are created. The primary file format used to document the structure of the human genome is the General Transfrer Format (GTF).

Documentation detailing the GTF file format can be found at the [ENSEMBL Website](http://m.ensembl.org/info/website/upload/gff.html).

**To orient yourself to the file format we will be using to identify gene structure this summer, I would like you to identify portions of several genes from a small gtf file I have created for you, "specific_genes.gtf".**

Specifically, for each gene in the gtf file, I would like for you to report: 
  1. The chromosome of the gene
  2. The gene start and end location in the chromosome
  3. The gene_id for the gene
  4. The transcript_id for each transcript associated with the gene\
      a. The transcript start and end location
  5. The exon coordinates for each exon associated with the gene\
      a. The transcript each exon is associated with
      
This should be reported in a markdown file. 

## Part 2

In this section, I would like for you to programmatically parse and report the data from part 1. Specifically, you will\
1. Read in the .gtf file specific_genes.gtf
2. Parse each line of the .gtf into a list such that each line is an element in the list
3. Print to genes_transcripts.txt the following content for each gene:
    a. the_gene_id chromosome_for_the_gene:the_gene_start:the_gene_end:the_gene_strand
5. Print to genes_transcripts.txt the following content for each transcript:
    b. the_gene_id_for_the_transcript chromosome_for_the_transcript:the_transcript_start:the_transcript_end:the_transcript_strand

