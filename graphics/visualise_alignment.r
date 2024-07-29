library(bios2mds)
see_alignment <- function (msf_alignment, graphix) 
{
    alignment <- import.msf(msf_alignment)
    print(alignment)
    distance_mat <- mat.dis(alignment, alignment)
    print(distance_mat)
 }
see_alignment('out.msf')