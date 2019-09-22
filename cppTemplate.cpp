/*
* Note: This template uses some c++11 functions , so you have to compile it with c++11 flag.
*       Example:-   $ g++ -std=c++11 main.cpp -o main
*
* On vjudge, use: C++14 (GCC 5.3.0)
*
*/
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
using namespace std;
int main()
{
  // Standard incantation to set up fast IO.
  ios::sync_with_stdio(false);
  cin.tie(0);
  // Simple example where we read a file where first line is an integer n, and after that
  // there are n lines each containing two integers and a string separated by a space.
  int n;
  cin >> n;  // read first line and parse the int value and save into n.
  // run the loop n times.
  for (int i = 0; i < n; i++) {
    int a, b;
    string s;
    cin >> a >> b >> s;
    // print sum of the ints followed by the original string, separated by space.
    int sum = a + b;
    cout << sum << " " << s << '\n';
  }
  // To run this example, create a file called, say, "input.txt":
  /*
    5
    1 2 foo
    3 4 bar
    5 6 baz
    7 8 moo
    9 10 azz
  */
  // Then compile the program:
  // g++ -std=c++11 main.cpp -o main
  // Then run it:
  // ./main < input.txt
  // You should get:
  /*
  3 foo
  7 bar
  11 baz
  15 moo
  19 azz
  */
  return 0;
}
