#!/usr/bin/python

## @logic.py
#  This file requires an input file, containing a 2-dimensional array (matrix)
#      of integers. Using the supplied matrix, this file determines the largest
#      possible sum of integers, from the upper-left to the lower-right corner,
#      with the restriction of only moving down, or to the right.
#
#  Note: sample input file(s) can be found in the 'data/' subdirectory
#
#  Note: this file returns both the path taken, and sum of each element traversed.
import sys, json

if __name__ == "__main__":

  # open, store data, close connection
  fp   = open(sys.argv[1])
  data = json.load( fp )
  fp.close()

  # local variables
  row_length = len(data) - 1
  col_length = len(data[0]) - 1
  row_range  = range(row_length + 1)
  col_range  = range(col_length + 1)
  list_max   = [[-1 for y in row_range] for x in col_range]
  list_path  = []

  # create summed matrix
  for i in row_range:
    for j in col_range:
      # base case:
      if i == 0 and j == 0:
        list_max[i][j] = data[i][j]
      # row case: add current cell, to top previous sum
      elif i == 0:
        list_max[i][j] = list_max[i][j-1] + data[i][j]
      # colummn case: add current cell, to left previous sum
      elif j == 0:
        list_max[i][j] = list_max[i-1][j] + data[i][j]
      # general case: add current cell, to previous greatest sum
      else:
        list_max[i][j] = max( list_max[i][j-1], list_max[i-1][j]) + data[i][j]

  # determine traveled path
  while row_length > 0 or col_length > 0:
    if row_length == 0:
      col_length -= 1
      list_path.append( 'R' )
    elif col_length == 0:
      row_length -= 1
      list_path.append( 'D' )
    elif list_max[row_length - 1][col_length] > list_max[row_length][col_length - 1]:
      row_length -= 1
      list_path.append( 'D' )
    elif list_max[row_length - 1][col_length] <= list_max[row_length][col_length - 1]:
      col_length -= 1
      list_path.append( 'R' )

  # return results
  print list_path[::-1]
  print max(list_max)[-1]
