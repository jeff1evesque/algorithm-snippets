Coding Challenge
================

A coding exercise was given to me when I applied for a *Software Engineer* role with [Grist Labs](http://www.getgrist.com/)

##Exercise

You are given a 2-dimensional grid of integers, like the example below. Consider the possible paths through the numbers, from the upper-left to the lower-right corner, that only move down or to the right. The value of a path is the sum of all the numbers that it visits. The goal is to find the path with the greatest value. If there is a tie, any one of such paths would do.

<table>
  <tbody>
    <tr>
      <td bgcolor='#90EE90'>0</td>
      <td>5</td>
      <td>0</td>
      <td>8</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <td bgcolor='#90EE90'>3</td>
      <td>6</td>
      <td>1</td>
      <td>3</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <td bgcolor='#90EE90'>9</td>
      <td>5</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td bgcolor='#90EE90'>8</td>
      <td bgcolor='#90EE90'>7</td>
      <td bgcolor='#90EE90'>9</td>
      <td>4</td>
      <td>8</td>
      <td>3</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td bgcolor='#90EE90'>7</td>
      <td bgcolor='#90EE90'>6</td>
      <td bgcolor='#90EE90'>2</td>
      <td bgcolor='#90EE90'>5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td bgcolor='#90EE90'>4</td>
    </tr>
  </tbody>
</table>

The specific grid for you to solve is given as a rectangular array of arrays in JSON format. The top-left corner is `array[0][0]`. You are to write a program, in a language of your choice, which finds a path with the largest sum, and outputs it as a string of characters: "R" for a step to the right, and "D" for a step down. Your program should also output the path's value.

For example, the sample above is available as [JSON here](https://github.com/jeff1evesque/algorithm-snippets/blob/master/greatest_path_sum/data/sample.json), and a correct solution to it is the highlighted path "DDDRRDRRRD", with the value of 60.

Here is the specific [challenge to solve](https://github.com/jeff1evesque/algorithm-snippets/blob/master/greatest_path_sum/data/sample2.json).
