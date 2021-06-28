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