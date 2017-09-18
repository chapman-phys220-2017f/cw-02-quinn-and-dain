# Instructor comments

Overall good. If you need help with notebook formatting, see the template in the info directory, or ask for tips. You have the right idea for describing what you are doing. The rest is streamlining the presentation and making it look prettier.

General notes:

 - Never use input(). Instead use command-line arguments, or an interactive notebook.
 - Interesting check: in your convergent sum, you terminate the summation when the next term is smaller than your tolerance. Did you check that the output sum changes only by digits smaller than this tolerance when you change the tolerance? As in if you set tol=1e-2 then tole-3, does only the third decimal digit change?
